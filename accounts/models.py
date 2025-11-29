from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import EmailValidator
from django.utils import timezone


class User(AbstractUser):
    USER_ROLE_CHOICES = (
        ('job_seeker', 'Job Seeker'),
        ('company', 'Company'),
    )
    
    role = models.CharField(max_length=20, choices=USER_ROLE_CHOICES, default='job_seeker')
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # Override the related_name to avoid conflicts
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='custom_user_groups',
        blank=True,
        help_text='The groups this user belongs to.'
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='custom_user_permissions',
        blank=True,
        help_text='Specific permissions for this user.'
    )

    class Meta:
        db_table = 'users'
        verbose_name_plural = 'Users'
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.username} ({self.get_role_display()})"

    def is_company(self):
        return self.role == 'company'

    def is_job_seeker(self):
        return self.role == 'job_seeker'


class JobSeeker(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='job_seeker_profile')
    bio = models.TextField(blank=True, null=True)
    resume = models.FileField(upload_to='resumes/', blank=True, null=True)
    skills = models.TextField(help_text="Enter skills separated by commas")
    experience_years = models.IntegerField(default=0)
    location = models.CharField(max_length=255)
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'job_seekers'
        verbose_name_plural = 'Job Seekers'

    def __str__(self):
        return f"{self.user.username} - Job Seeker"

    def get_skills_list(self):
        return [skill.strip() for skill in self.skills.split(',') if skill.strip()]
