from django.db import models
from companies.models import Company
from django.utils import timezone


class Job(models.Model):
    JOB_TYPE_CHOICES = (
        ('full_time', 'Full Time'),
        ('part_time', 'Part Time'),
        ('contract', 'Contract'),
        ('internship', 'Internship'),
    )

    EXPERIENCE_LEVEL_CHOICES = (
        ('entry', 'Entry Level'),
        ('mid', 'Mid Level'),
        ('senior', 'Senior'),
        ('executive', 'Executive'),
    )

    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='jobs')
    title = models.CharField(max_length=255)
    description = models.TextField()
    requirements = models.TextField(help_text="Enter requirements separated by newlines")
    location = models.CharField(max_length=255)
    salary_min = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    salary_max = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    job_type = models.CharField(max_length=20, choices=JOB_TYPE_CHOICES)
    experience_level = models.CharField(max_length=20, choices=EXPERIENCE_LEVEL_CHOICES)
    is_active = models.BooleanField(default=True)
    posted_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deadline = models.DateTimeField(blank=True, null=True)
    total_positions = models.IntegerField(default=1)

    class Meta:
        db_table = 'jobs'
        verbose_name_plural = 'Jobs'
        ordering = ['-posted_at']
        indexes = [
            models.Index(fields=['company', 'is_active']),
            models.Index(fields=['job_type']),
        ]

    def __str__(self):
        return f"{self.title} at {self.company.company_name}"

    def is_application_deadline_passed(self):
        if self.deadline:
            return timezone.now() > self.deadline
        return False

    def get_salary_range(self):
        if self.salary_min and self.salary_max:
            return f"NPR {self.salary_min:,.0f} - NPR {self.salary_max:,.0f}"
        elif self.salary_min:
            return f"From NPR {self.salary_min:,.0f}"
        elif self.salary_max:
            return f"Up to NPR {self.salary_max:,.0f}"
        return "Salary Not Specified"

    def get_requirements_list(self):
        return [req.strip() for req in self.requirements.split('\n') if req.strip()]

    def get_total_applications(self):
        return self.applications.count()
