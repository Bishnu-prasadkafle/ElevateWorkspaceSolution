from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_protect
from .models import User, JobSeeker
from companies.models import Company


@require_http_methods(["GET", "POST"])
@csrf_protect
def register(request):
    """Handle user registration for both job seekers and companies"""
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        user_type = request.POST.get('user_type', 'job_seeker')
        phone_number = request.POST.get('phone_number', '')
        
        # Validation
        if not all([username, email, password1, password2]):
            messages.error(request, 'All fields are required.')
            return render(request, 'accounts/register.html')
        
        if password1 != password2:
            messages.error(request, 'Passwords do not match.')
            return render(request, 'accounts/register.html')
        
        if len(password1) < 8:
            messages.error(request, 'Password must be at least 8 characters long.')
            return render(request, 'accounts/register.html')
        
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists.')
            return render(request, 'accounts/register.html')
        
        if User.objects.filter(email=email).exists():
            messages.error(request, 'Email already registered.')
            return render(request, 'accounts/register.html')
        
        try:
            # Create user
            user = User.objects.create_user(
                username=username,
                email=email,
                password=password1,
                role=user_type,
                phone_number=phone_number,
                first_name=request.POST.get('first_name', ''),
                last_name=request.POST.get('last_name', '')
            )

            # Create corresponding profile
            if user_type == 'job_seeker':
                JobSeeker.objects.create(
                    user=user,
                    location=request.POST.get('location', ''),
                    skills=request.POST.get('skills', '')
                )
                messages.success(request, 'Job Seeker account created successfully!')
            else:  # company
                Company.objects.create(
                    user=user,
                    company_name=request.POST.get('company_name', ''),
                    industry=request.POST.get('industry', ''),
                    location=request.POST.get('location', ''),
                    description=request.POST.get('description', '')
                )
                messages.success(request, 'Company account created successfully!')

            # Automatically log the user in after successful registration
            try:
                login(request, user)
            except Exception:
                # If auto-login fails for any reason, fall back to login page
                return redirect('accounts:login')

            # Redirect based on role
            if user.is_company():
                return redirect('application:company_dashboard')
            else:
                return redirect('jobs:job_list')
        
        except Exception as e:
            messages.error(request, f'Error during registration: {str(e)}')
            return render(request, 'accounts/register.html')
    
    return render(request, 'accounts/register.html')


@require_http_methods(["GET", "POST"])
@csrf_protect
def login_view(request):
    """Handle user login"""
    if request.user.is_authenticated:
        # Redirect authenticated users based on role
        if request.user.is_company():
            return redirect('application:company_dashboard')
        else:
            return redirect('jobs:job_list')
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        if not username or not password:
            messages.error(request, 'Username and password are required.')
            return render(request, 'accounts/login.html')
        
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            if not user.is_active:
                messages.error(request, 'Your account is disabled.')
                return render(request, 'accounts/login.html')
            
            login(request, user)
            messages.success(request, f'Welcome back, {user.username}!')
            
            # Redirect based on user role
            if user.is_company():
                return redirect('application:company_dashboard')
            else:
                return redirect('jobs:job_list')
        else:
            messages.error(request, 'Invalid username or password.')
            return render(request, 'accounts/login.html')
    
    return render(request, 'accounts/login.html')


def logout_view(request):
    """Handle user logout"""
    if request.user.is_authenticated:
        logout(request)
        messages.success(request, 'You have been logged out successfully.')
    return redirect('home')


@login_required(login_url='accounts:login')
def profile(request):
    """Display user profile"""
    context = {}
    
    if request.user.is_company():
        try:
            context['company'] = request.user.company_profile
        except Company.DoesNotExist:
            pass
    else:
        try:
            context['job_seeker'] = request.user.job_seeker_profile
        except JobSeeker.DoesNotExist:
            pass
    
    context['user'] = request.user
    return render(request, 'accounts/profile.html', context)


@login_required(login_url='accounts:login')
@require_http_methods(["GET", "POST"])
def profile_edit(request):
    """Edit user profile"""
    if request.method == 'POST':
        request.user.first_name = request.POST.get('first_name', request.user.first_name)
        request.user.last_name = request.POST.get('last_name', request.user.last_name)
        request.user.email = request.POST.get('email', request.user.email)
        request.user.phone_number = request.POST.get('phone_number', request.user.phone_number)
        request.user.save()
        
        if request.user.is_company():
            company = request.user.company_profile
            company.company_name = request.POST.get('company_name', company.company_name)
            company.industry = request.POST.get('industry', company.industry)
            company.location = request.POST.get('location', company.location)
            company.description = request.POST.get('description', company.description)
            company.website = request.POST.get('website', company.website)
            company.save()
        else:
            job_seeker = request.user.job_seeker_profile
            job_seeker.location = request.POST.get('location', job_seeker.location)
            job_seeker.skills = request.POST.get('skills', job_seeker.skills)
            job_seeker.experience_years = int(request.POST.get('experience_years', job_seeker.experience_years))
            job_seeker.bio = request.POST.get('bio', job_seeker.bio)
            job_seeker.save()
        
        messages.success(request, 'Profile updated successfully!')
        return redirect('profile')
    
    context = {'user': request.user}
    
    if request.user.is_company():
        try:
            context['company'] = request.user.company_profile
        except Company.DoesNotExist:
            pass
    else:
        try:
            context['job_seeker'] = request.user.job_seeker_profile
        except JobSeeker.DoesNotExist:
            pass
    
    return render(request, 'accounts/profile_edit.html', context)
