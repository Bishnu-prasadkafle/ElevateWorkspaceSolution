from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from django.views.decorators.http import require_http_methods
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from .models import User, JobSeeker
from companies.models import Company


def is_admin(user):
    """Check if user is admin (superuser)"""
    return user.is_superuser and user.is_staff


@login_required(login_url='accounts:login')
@user_passes_test(is_admin, login_url='accounts:login')
def admin_dashboard(request):
    """Admin dashboard overview"""
    total_users = User.objects.count()
    total_job_seekers = JobSeeker.objects.count()
    total_companies = Company.objects.count()
    total_active_users = User.objects.filter(is_active=True).count()
    
    recent_users = User.objects.all().order_by('-created_at')[:5]
    recent_companies = Company.objects.all().order_by('-created_at')[:5]
    
    context = {
        'total_users': total_users,
        'total_job_seekers': total_job_seekers,
        'total_companies': total_companies,
        'total_active_users': total_active_users,
        'recent_users': recent_users,
        'recent_companies': recent_companies,
    }
    
    return render(request, 'admin/dashboard.html', context)


@login_required(login_url='accounts:login')
@user_passes_test(is_admin, login_url='accounts:login')
def manage_users(request):
    """Manage all users (job seekers and companies)"""
    users = User.objects.all().order_by('-created_at')
    
    role_filter = request.GET.get('role', '')
    if role_filter:
        users = users.filter(role=role_filter)
    
    search_query = request.GET.get('search', '')
    if search_query:
        users = users.filter(
            Q(username__icontains=search_query) | 
            Q(email__icontains=search_query)
        )
    
    paginator = Paginator(users, 20)
    page_number = request.GET.get('page')
    
    try:
        page_obj = paginator.page(page_number)
    except PageNotAnInteger:
        page_obj = paginator.page(1)
    except EmptyPage:
        page_obj = paginator.page(paginator.num_pages)
    
    context = {
        'page_obj': page_obj,
        'users': page_obj.object_list,
        'role_filter': role_filter,
        'search_query': search_query,
    }
    
    return render(request, 'admin/manage_users.html', context)


@login_required(login_url='accounts:login')
@user_passes_test(is_admin, login_url='accounts:login')
@require_http_methods(["GET", "POST"])
def add_user(request):
    """Add a new user (job seeker or company)"""
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        first_name = request.POST.get('first_name', '')
        last_name = request.POST.get('last_name', '')
        phone_number = request.POST.get('phone_number', '')
        user_type = request.POST.get('user_type', 'job_seeker')
        
        if not all([username, email, password, user_type]):
            messages.error(request, 'Username, email, password, and user type are required.')
            return render(request, 'admin/add_user.html')
        
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists.')
            return render(request, 'admin/add_user.html')
        
        if User.objects.filter(email=email).exists():
            messages.error(request, 'Email already registered.')
            return render(request, 'admin/add_user.html')
        
        try:
            user = User.objects.create_user(
                username=username,
                email=email,
                password=password,
                first_name=first_name,
                last_name=last_name,
                phone_number=phone_number,
                role=user_type,
                is_active=True,
            )
            
            if user_type == 'job_seeker':
                location = request.POST.get('location', '')
                skills = request.POST.get('skills', '')
                JobSeeker.objects.create(
                    user=user,
                    location=location,
                    skills=skills
                )
            else:
                company_name = request.POST.get('company_name', '')
                industry = request.POST.get('industry', '')
                location = request.POST.get('location', '')
                description = request.POST.get('description', '')
                Company.objects.create(
                    user=user,
                    company_name=company_name,
                    industry=industry,
                    location=location,
                    description=description,
                )
            
            messages.success(request, f'{user_type.replace("_", " ").title()} created successfully!')
            return redirect('accounts:manage_users')
        
        except Exception as e:
            messages.error(request, f'Error creating user: {str(e)}')
            return render(request, 'admin/add_user.html')
    
    return render(request, 'admin/add_user.html')


@login_required(login_url='accounts:login')
@user_passes_test(is_admin, login_url='accounts:login')
@require_http_methods(["GET", "POST"])
def edit_user(request, pk):
    """Edit user details"""
    user = get_object_or_404(User, pk=pk)
    
    if request.method == 'POST':
        user.first_name = request.POST.get('first_name', user.first_name)
        user.last_name = request.POST.get('last_name', user.last_name)
        user.email = request.POST.get('email', user.email)
        user.phone_number = request.POST.get('phone_number', user.phone_number)
        user.is_active = request.POST.get('is_active') == 'on'
        user.save()
        
        if user.is_job_seeker():
            try:
                job_seeker = user.job_seeker_profile
                job_seeker.location = request.POST.get('location', job_seeker.location)
                job_seeker.skills = request.POST.get('skills', job_seeker.skills)
                job_seeker.save()
            except JobSeeker.DoesNotExist:
                pass
        else:
            try:
                company = user.company_profile
                company.company_name = request.POST.get('company_name', company.company_name)
                company.industry = request.POST.get('industry', company.industry)
                company.location = request.POST.get('location', company.location)
                company.description = request.POST.get('description', company.description)
                company.save()
            except Company.DoesNotExist:
                pass
        
        messages.success(request, 'User updated successfully!')
        return redirect('accounts:manage_users')
    
    context = {
        'user': user,
        'job_seeker': None,
        'company': None,
    }
    
    if user.is_job_seeker():
        try:
            context['job_seeker'] = user.job_seeker_profile
        except JobSeeker.DoesNotExist:
            pass
    else:
        try:
            context['company'] = user.company_profile
        except Company.DoesNotExist:
            pass
    
    return render(request, 'admin/edit_user.html', context)


@login_required(login_url='accounts:login')
@user_passes_test(is_admin, login_url='accounts:login')
@require_http_methods(["POST"])
def delete_user(request, pk):
    """Delete a user"""
    user = get_object_or_404(User, pk=pk)
    
    username = user.username
    user.delete()
    
    messages.success(request, f'User "{username}" has been deleted successfully.')
    return redirect('accounts:manage_users')


@login_required(login_url='accounts:login')
@user_passes_test(is_admin, login_url='accounts:login')
def manage_companies(request):
    """Manage all companies"""
    companies = Company.objects.all().order_by('-created_at')
    
    status_filter = request.GET.get('status', '')
    if status_filter:
        companies = companies.filter(status=status_filter)
    
    verified_filter = request.GET.get('verified', '')
    if verified_filter:
        companies = companies.filter(verified=verified_filter == 'true')
    
    search_query = request.GET.get('search', '')
    if search_query:
        companies = companies.filter(
            company_name__icontains=search_query
        )
    
    paginator = Paginator(companies, 20)
    page_number = request.GET.get('page')
    
    try:
        page_obj = paginator.page(page_number)
    except PageNotAnInteger:
        page_obj = paginator.page(1)
    except EmptyPage:
        page_obj = paginator.page(paginator.num_pages)
    
    context = {
        'page_obj': page_obj,
        'companies': page_obj.object_list,
        'status_filter': status_filter,
        'verified_filter': verified_filter,
        'search_query': search_query,
    }
    
    return render(request, 'admin/manage_companies.html', context)


@login_required(login_url='accounts:login')
@user_passes_test(is_admin, login_url='accounts:login')
@require_http_methods(["GET", "POST"])
def edit_company(request, pk):
    """Edit company details"""
    company = get_object_or_404(Company, pk=pk)
    
    if request.method == 'POST':
        company.company_name = request.POST.get('company_name', company.company_name)
        company.industry = request.POST.get('industry', company.industry)
        company.location = request.POST.get('location', company.location)
        company.description = request.POST.get('description', company.description)
        company.website = request.POST.get('website', company.website)
        company.status = request.POST.get('status', company.status)
        company.verified = request.POST.get('verified') == 'on'
        company.save()
        
        messages.success(request, 'Company updated successfully!')
        return redirect('accounts:manage_companies')
    
    context = {
        'company': company,
    }
    
    return render(request, 'admin/edit_company.html', context)


@login_required(login_url='accounts:login')
@user_passes_test(is_admin, login_url='accounts:login')
@require_http_methods(["POST"])
def delete_company(request, pk):
    """Delete a company"""
    company = get_object_or_404(Company, pk=pk)
    
    company_name = company.company_name
    company.delete()
    
    messages.success(request, f'Company "{company_name}" has been deleted successfully.')
    return redirect('accounts:manage_companies')


@login_required(login_url='accounts:login')
@user_passes_test(is_admin, login_url='accounts:login')
@require_http_methods(["POST"])
def toggle_user_status(request, pk):
    """Toggle user active status"""
    user = get_object_or_404(User, pk=pk)
    user.is_active = not user.is_active
    user.save()
    
    status = 'activated' if user.is_active else 'deactivated'
    messages.success(request, f'User "{user.username}" has been {status}.')
    return redirect('accounts:manage_users')


@login_required(login_url='accounts:login')
@user_passes_test(is_admin, login_url='accounts:login')
@require_http_methods(["POST"])
def toggle_company_verification(request, pk):
    """Toggle company verification status"""
    company = get_object_or_404(Company, pk=pk)
    company.verified = not company.verified
    company.save()
    
    status = 'verified' if company.verified else 'unverified'
    messages.success(request, f'Company "{company.company_name}" has been {status}.')
    return redirect('accounts:manage_companies')
