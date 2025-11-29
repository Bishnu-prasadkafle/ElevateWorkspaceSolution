from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.views.decorators.http import require_http_methods
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from jobs.models import Job
from .models import JobApplication


@login_required(login_url='accounts:login')
@require_http_methods(["GET", "POST"])
def apply_job(request, job_id):
    """Submit a job application"""
    job = get_object_or_404(Job, pk=job_id, is_active=True)
    
    # Check if user is a job seeker
    if not request.user.is_job_seeker():
        messages.error(request, 'Only job seekers can apply for jobs.')
        return redirect('jobs:job_detail', pk=job_id)
    
    try:
        job_seeker = request.user.job_seeker_profile
    except:
        messages.error(request, 'Job seeker profile not found.')
        return redirect('jobs:job_detail', pk=job_id)
    
    # Check if already applied
    if JobApplication.objects.filter(job=job, job_seeker=job_seeker).exists():
        messages.warning(request, 'You have already applied for this job.')
        return redirect('jobs:job_detail', pk=job_id)
    
    # Check if deadline passed
    if job.is_application_deadline_passed():
        messages.error(request, 'Application deadline has passed.')
        return redirect('jobs:job_detail', pk=job_id)
    
    if request.method == 'POST':
        try:
            cover_letter = request.POST.get('cover_letter', '')
            
            application = JobApplication.objects.create(
                job=job,
                job_seeker=job_seeker,
                cover_letter=cover_letter,
                status='pending'
            )
            
            messages.success(request, 'Your application has been submitted successfully!')
            return redirect('application:application_detail', pk=application.pk)
        
        except Exception as e:
            messages.error(request, f'Error submitting application: {str(e)}')
            return redirect('jobs:job_detail', pk=job_id)
    
    context = {
        'job': job,
    }
    
    return render(request, 'application/apply_job.html', context)


@login_required(login_url='accounts:login')
def application_detail(request, pk):
    """Display application details"""
    application = get_object_or_404(JobApplication, pk=pk)
    
    # Check permissions
    is_applicant = (request.user.is_job_seeker() and 
                   application.job_seeker.user == request.user)
    is_company = (request.user.is_company() and 
                 application.job.company.user == request.user)
    
    if not (is_applicant or is_company):
        messages.error(request, 'You do not have permission to view this application.')
        return redirect('jobs:job_list')
    
    context = {
        'application': application,
        'is_applicant': is_applicant,
        'is_company': is_company,
    }
    
    return render(request, 'application/application_detail.html', context)


@login_required(login_url='accounts:login')
def my_applications(request):
    """Display job seeker's applications"""
    if not request.user.is_job_seeker():
        messages.error(request, 'This page is for job seekers only.')
        return redirect('jobs:job_list')
    
    try:
        job_seeker = request.user.job_seeker_profile
    except:
        messages.error(request, 'Job seeker profile not found.')
        return redirect('jobs:job_list')
    
    # Filter applications
    applications = JobApplication.objects.filter(
        job_seeker=job_seeker
    ).select_related('job', 'job__company').order_by('-applied_at')
    
    # Status filter
    status_filter = request.GET.get('status', '')
    if status_filter:
        applications = applications.filter(status=status_filter)
    
    # Pagination
    paginator = Paginator(applications, 10)
    page_number = request.GET.get('page')
    
    try:
        page_obj = paginator.page(page_number)
    except PageNotAnInteger:
        page_obj = paginator.page(1)
    except EmptyPage:
        page_obj = paginator.page(paginator.num_pages)
    
    context = {
        'page_obj': page_obj,
        'applications': page_obj.object_list,
        'status_filter': status_filter,
    }
    
    return render(request, 'application/my_applications.html', context)


@login_required(login_url='accounts:login')
@require_http_methods(["POST"])
def withdraw_application(request, pk):
    """Withdraw a job application"""
    application = get_object_or_404(JobApplication, pk=pk)
    
    # Check if user is the applicant
    if application.job_seeker.user != request.user:
        messages.error(request, 'You do not have permission to withdraw this application.')
        return redirect('application:my_applications')
    
    if not application.can_be_withdrawn():
        messages.error(request, 'This application cannot be withdrawn.')
        return redirect('application:application_detail', pk=pk)
    
    try:
        application.status = 'withdrawn'
        application.save()
        messages.success(request, 'Application withdrawn successfully!')
        return redirect('application:my_applications')
    except Exception as e:
        messages.error(request, f'Error withdrawing application: {str(e)}')
        return redirect('application:application_detail', pk=pk)


@login_required(login_url='accounts:login')
@require_http_methods(["GET", "POST"])
def update_application_status(request, pk):
    """Update application status (for companies)"""
    application = get_object_or_404(JobApplication, pk=pk)
    
    # Check if user is the company owner
    if application.job.company.user != request.user:
        messages.error(request, 'You do not have permission to update this application.')
        return redirect('jobs:job_list')
    
    if request.method == 'POST':
        new_status = request.POST.get('status')
        
        if new_status not in dict(application.APPLICATION_STATUS_CHOICES):
            messages.error(request, 'Invalid status.')
            return redirect('application:application_detail', pk=pk)
        
        try:
            application.status = new_status
            application.save()
            messages.success(request, f'Application status updated to {new_status}!')
            return redirect('application:application_detail', pk=pk)
        except Exception as e:
            messages.error(request, f'Error updating status: {str(e)}')
            return redirect('application:application_detail', pk=pk)
    
    context = {
        'application': application,
        'status_choices': application.APPLICATION_STATUS_CHOICES,
    }
    
    return render(request, 'application/update_status.html', context)


@login_required(login_url='login')
def company_dashboard(request):
    """Company dashboard displaying jobs and applications"""
    if not request.user.is_company():
        messages.error(request, 'This page is for companies only.')
        return redirect('jobs:job_list')
    
    try:
        company = request.user.company_profile
    except:
        messages.error(request, 'Company profile not found.')
        return redirect('jobs:job_list')
    
    # Get company's jobs
    jobs = company.jobs.all().order_by('-posted_at')
    
    # Get all applications for company's jobs
    applications = JobApplication.objects.filter(
        job__company=company
    ).select_related('job', 'job_seeker').order_by('-applied_at')
    
    # Status filter
    status_filter = request.GET.get('status', '')
    if status_filter:
        applications = applications.filter(status=status_filter)
    
    # Pagination for applications
    paginator = Paginator(applications, 10)
    page_number = request.GET.get('page')
    
    try:
        page_obj = paginator.page(page_number)
    except PageNotAnInteger:
        page_obj = paginator.page(1)
    except EmptyPage:
        page_obj = paginator.page(paginator.num_pages)
    
    context = {
        'company': company,
        'jobs': jobs,
        'page_obj': page_obj,
        'applications': page_obj.object_list,
        'status_filter': status_filter,
        'total_jobs': jobs.count(),
        'active_jobs': jobs.filter(is_active=True).count(),
        'total_applications': applications.count(),
        'pending_applications': applications.filter(status='pending').count(),
    }
    
    return render(request, 'application/company_dashboard.html', context)
