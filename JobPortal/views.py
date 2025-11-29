from django.shortcuts import render
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
