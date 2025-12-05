from django.db import models
from accounts.models import JobSeeker, User
from jobs.models import Job
from django.utils import timezone


class JobApplication(models.Model):
    APPLICATION_STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('reviewed', 'Reviewed'),
        ('shortlisted', 'Shortlisted'),
        ('rejected', 'Rejected'),
        ('accepted', 'Accepted'),
        ('withdrawn', 'Withdrawn'),
    )

    job = models.ForeignKey(Job, on_delete=models.CASCADE, related_name='applications')
    job_seeker = models.ForeignKey(JobSeeker, on_delete=models.CASCADE, related_name='applications')
    status = models.CharField(max_length=20, choices=APPLICATION_STATUS_CHOICES, default='pending')
    cover_letter = models.TextField(blank=True, null=True)
    resume = models.FileField(upload_to='applications/resumes/', blank=True, null=True)
    applied_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = 'job_applications'
        verbose_name_plural = 'Job Applications'
        ordering = ['-applied_at']
        unique_together = ['job', 'job_seeker']
        indexes = [
            models.Index(fields=['job', 'status']),
            models.Index(fields=['job_seeker', 'status']),
        ]

    def __str__(self):
        return f"{self.job_seeker.user.username} applied for {self.job.title}"

    def get_status_badge_color(self):
        """Returns Bootstrap color class for status badge"""
        color_map = {
            'pending': 'warning',
            'reviewed': 'info',
            'shortlisted': 'success',
            'rejected': 'danger',
            'accepted': 'success',
            'withdrawn': 'secondary',
        }
        return color_map.get(self.status, 'secondary')

    def can_be_withdrawn(self):
        """Check if application can be withdrawn"""
        return self.status not in ['rejected', 'accepted', 'withdrawn']

    def get_days_since_applied(self):
        """Get number of days since application was submitted"""
        delta = timezone.now() - self.applied_at
        return delta.days


class ApplicationDocument(models.Model):
    """Additional documents uploaded for an application (CV, certificates, portfolio etc.)"""
    application = models.ForeignKey(JobApplication, on_delete=models.CASCADE, related_name='documents')
    file = models.FileField(upload_to='applications/documents/')
    label = models.CharField(max_length=150, blank=True, null=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-uploaded_at']

    def __str__(self):
        return f"Document for {self.application} - {self.file.name.split('/')[-1]}"
