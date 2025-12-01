from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages
from jobs.models import Job


def home(request):
    """Home page showing featured jobs"""
    featured_jobs = Job.objects.filter(is_active=True).order_by('-posted_at')[:6]
    total_jobs = Job.objects.filter(is_active=True).count()
    
    context = {
        'featured_jobs': featured_jobs,
        'total_jobs': total_jobs,
    }
    
    return render(request, 'home.html', context)


def about(request):
    """About page view"""
    context = {
        'team_size': '50+',
        'companies': '500+',
        'job_postings': Job.objects.count(),
        'placements': '1000+',
    }
    return render(request, 'about.html', context)


def services(request):
    """Services page view"""
    services_list = [
        {
            'title': 'Job Posting',
            'description': 'Companies can post job openings with detailed job descriptions, requirements, and benefits.',
            'icon': 'fa-briefcase',
            'color': '#3498db'
        },
        {
            'title': 'Job Search',
            'description': 'Job seekers can search and filter jobs by location, industry, experience level, and salary.',
            'icon': 'fa-search',
            'color': '#2ecc71'
        },
        {
            'title': 'Application Management',
            'description': 'Track applications, manage candidates, and communicate with job seekers seamlessly.',
            'icon': 'fa-file-alt',
            'color': '#e74c3c'
        },
        {
            'title': 'Profile Management',
            'description': 'Create and manage professional profiles with resume upload, skills, and work experience.',
            'icon': 'fa-user-tie',
            'color': '#f39c12'
        },
        {
            'title': 'Secure Authentication',
            'description': 'Advanced security measures to protect user data and ensure safe transactions.',
            'icon': 'fa-lock',
            'color': '#9b59b6'
        },
        {
            'title': 'Company Dashboard',
            'description': 'Comprehensive analytics and insights for company hiring needs and trends.',
            'icon': 'fa-chart-bar',
            'color': '#1abc9c'
        },
    ]
    context = {'services': services_list}
    return render(request, 'services.html', context)


def contact(request):
    """Contact page view with email handling"""
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        phone = request.POST.get('phone', '')
        
        # Validate form data
        if not all([name, email, subject, message]):
            messages.error(request, 'Please fill in all required fields.')
            return render(request, 'contact.html')
        
        # Prepare email
        email_subject = f"New Contact Form Submission: {subject}"
        email_body = f"""
New message from {name}

Email: {email}
Phone: {phone}
Subject: {subject}

Message:
{message}
        """
        
        try:
            # Send email to admin
            send_mail(
                email_subject,
                email_body,
                settings.DEFAULT_FROM_EMAIL,
                [settings.CONTACT_EMAIL],
                fail_silently=False,
            )
            
            # Send confirmation email to user
            confirmation_body = f"""
Dear {name},

Thank you for contacting Elevate Workforce Solutions. We have received your message and will get back to you as soon as possible.

Your Message:
Subject: {subject}
Message: {message}

Best regards,
Elevate Workforce Solutions Team
            """
            
            send_mail(
                'We received your message - Elevate Workforce Solutions',
                confirmation_body,
                settings.DEFAULT_FROM_EMAIL,
                [email],
                fail_silently=False,
            )
            
            messages.success(request, 'Your message has been sent successfully! We will contact you soon.')
            return render(request, 'contact.html', {'form_submitted': True})
        except Exception as e:
            messages.error(request, f'Error sending email: {str(e)}')
    
    context = {
        'email': 'info@elevateworkforce.com',
        'phone': '+977-1-XXXX-XXXX',
        'address': 'Kathmandu, Nepal'
    }
    return render(request, 'contact.html', context)
