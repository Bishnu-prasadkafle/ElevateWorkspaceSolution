from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.views.decorators.http import require_http_methods
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from .models import Job
from application.models import JobApplication


def job_list(request):
    """Display all active job listings with pagination and filtering"""
    jobs = Job.objects.filter(is_active=True).select_related('company')
    
    # Search filter
    search_query = request.GET.get('search', '')
    if search_query:
        jobs = jobs.filter(
            Q(title__icontains=search_query) |
            Q(description__icontains=search_query) |
            Q(company__company_name__icontains=search_query)
        )
    
    # Job type filter
    job_type = request.GET.get('job_type', '')
    if job_type:
        jobs = jobs.filter(job_type=job_type)
    
    # Location filter
    location = request.GET.get('location', '')
    if location:
        jobs = jobs.filter(location__icontains=location)
    
    # Experience level filter
    experience_level = request.GET.get('experience_level', '')
    if experience_level:
        jobs = jobs.filter(experience_level=experience_level)
    
    # Pagination
    paginator = Paginator(jobs, 10)  # 10 jobs per page
    page_number = request.GET.get('page')
    
    try:
        page_obj = paginator.page(page_number)
    except PageNotAnInteger:
        page_obj = paginator.page(1)
    except EmptyPage:
        page_obj = paginator.page(paginator.num_pages)
    
    context = {
        'page_obj': page_obj,
        'jobs': page_obj.object_list,
        'search_query': search_query,
        'job_type': job_type,
        'location': location,
        'experience_level': experience_level,
    }
    
    return render(request, 'jobs/job_list.html', context)


def job_detail(request, pk):
    """Display detailed view of a specific job"""
    job = get_object_or_404(Job, pk=pk, is_active=True)
    user_has_applied = False
    
    if request.user.is_authenticated and request.user.is_job_seeker():
        try:
            user_job_seeker = request.user.job_seeker_profile
            user_has_applied = JobApplication.objects.filter(
                job=job,
                job_seeker=user_job_seeker
            ).exists()
        except:
            pass
    
    context = {
        'job': job,
        'user_has_applied': user_has_applied,
    }
    
    return render(request, 'jobs/job_detail.html', context)


@login_required(login_url='login')
@require_http_methods(["GET", "POST"])
def create_job(request):
    """Create a new job posting (only for companies)"""
    if not request.user.is_company():
        messages.error(request, 'Only companies can post jobs.')
        return redirect('job_list')
    
    try:
        company = request.user.company_profile
    except:
        messages.error(request, 'Company profile not found.')
        return redirect('job_list')
    
    if request.method == 'POST':
        try:
            job = Job.objects.create(
                company=company,
                title=request.POST.get('title'),
                description=request.POST.get('description'),
                requirements=request.POST.get('requirements'),
                location=request.POST.get('location'),
                job_type=request.POST.get('job_type'),
                experience_level=request.POST.get('experience_level'),
                total_positions=int(request.POST.get('total_positions', 1)),
                salary_min=request.POST.get('salary_min') or None,
                salary_max=request.POST.get('salary_max') or None,
                deadline=request.POST.get('deadline') or None,
            )
            messages.success(request, 'Job posted successfully!')
            return redirect('job_detail', pk=job.pk)
        
        except Exception as e:
            messages.error(request, f'Error posting job: {str(e)}')
            return render(request, 'jobs/create_job.html')
    
    context = {
        'job_types': Job.JOB_TYPE_CHOICES,
        'experience_levels': Job.EXPERIENCE_LEVEL_CHOICES,
    }
    
    return render(request, 'jobs/create_job.html', context)


@login_required(login_url='login')
@require_http_methods(["GET", "POST"])
def edit_job(request, pk):
    """Edit an existing job posting"""
    job = get_object_or_404(Job, pk=pk)
    
    # Check if user is the company owner
    if not request.user.is_company() or job.company.user != request.user:
        messages.error(request, 'You do not have permission to edit this job.')
        return redirect('job_list')
    
    if request.method == 'POST':
        try:
            job.title = request.POST.get('title', job.title)
            job.description = request.POST.get('description', job.description)
            job.requirements = request.POST.get('requirements', job.requirements)
            job.location = request.POST.get('location', job.location)
            job.job_type = request.POST.get('job_type', job.job_type)
            job.experience_level = request.POST.get('experience_level', job.experience_level)
            job.total_positions = int(request.POST.get('total_positions', job.total_positions))
            job.salary_min = request.POST.get('salary_min') or None
            job.salary_max = request.POST.get('salary_max') or None
            job.deadline = request.POST.get('deadline') or None
            job.save()
            
            messages.success(request, 'Job updated successfully!')
            return redirect('job_detail', pk=job.pk)
        
        except Exception as e:
            messages.error(request, f'Error updating job: {str(e)}')
    
    context = {
        'job': job,
        'job_types': Job.JOB_TYPE_CHOICES,
        'experience_levels': Job.EXPERIENCE_LEVEL_CHOICES,
    }
    
    return render(request, 'jobs/edit_job.html', context)


@login_required(login_url='login')
@require_http_methods(["POST"])
def delete_job(request, pk):
    """Delete a job posting"""
    job = get_object_or_404(Job, pk=pk)
    
    # Check if user is the company owner
    if not request.user.is_company() or job.company.user != request.user:
        messages.error(request, 'You do not have permission to delete this job.')
        return redirect('job_list')
    
    try:
        job_title = job.title
        job.delete()
        messages.success(request, f'Job "{job_title}" deleted successfully!')
        return redirect('company_dashboard')
    except Exception as e:
        messages.error(request, f'Error deleting job: {str(e)}')
        return redirect('job_detail', pk=job.pk)


@login_required(login_url='login')
@require_http_methods(["POST"])
def toggle_job_status(request, pk):
    """Toggle job active/inactive status"""
    job = get_object_or_404(Job, pk=pk)
    
    # Check if user is the company owner
    if not request.user.is_company() or job.company.user != request.user:
        messages.error(request, 'You do not have permission to modify this job.')
        return redirect('job_list')
    
    try:
        job.is_active = not job.is_active
        job.save()
        status_text = "activated" if job.is_active else "deactivated"
        messages.success(request, f'Job {status_text} successfully!')
        return redirect('company_dashboard')
    except Exception as e:
        messages.error(request, f'Error updating job status: {str(e)}')
        return redirect('job_detail', pk=job.pk)
