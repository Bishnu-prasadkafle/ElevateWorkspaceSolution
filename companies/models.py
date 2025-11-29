from django.db import models
from accounts.models import User


class Company(models.Model):
    COMPANY_STATUS_CHOICES = (
        ('active', 'Active'),
        ('inactive', 'Inactive'),
        ('suspended', 'Suspended'),
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='company_profile')
    company_name = models.CharField(max_length=255, unique=True)
    description = models.TextField()
    website = models.URLField(blank=True, null=True)
    industry = models.CharField(max_length=100)
    location = models.CharField(max_length=255)
    company_size = models.CharField(max_length=50, blank=True, null=True)
    logo = models.ImageField(upload_to='company_logos/', blank=True, null=True)
    status = models.CharField(max_length=20, choices=COMPANY_STATUS_CHOICES, default='active')
    verified = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'companies'
        verbose_name_plural = 'Companies'
        ordering = ['-created_at']

    def __str__(self):
        return self.company_name

    def is_active_company(self):
        return self.status == 'active' and self.verified

    def get_total_jobs_posted(self):
        return self.jobs.count()

    def get_active_jobs(self):
        return self.jobs.filter(is_active=True)
