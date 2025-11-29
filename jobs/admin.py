from django.contrib import admin
from .models import Job


@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = ('title', 'company', 'job_type', 'experience_level', 'is_active', 'posted_at')
    list_filter = ('job_type', 'experience_level', 'is_active', 'posted_at')
    search_fields = ('title', 'description', 'company__company_name', 'location')
    fieldsets = (
        ('Job Information', {'fields': ('company', 'title', 'description')}),
        ('Job Details', {'fields': ('job_type', 'experience_level', 'total_positions')}),
        ('Location & Salary', {'fields': ('location', 'salary_min', 'salary_max')}),
        ('Requirements', {'fields': ('requirements',)}),
        ('Status', {'fields': ('is_active', 'deadline')}),
        ('Timestamps', {'fields': ('posted_at', 'updated_at'), 'classes': ('collapse',)}),
    )
    readonly_fields = ('posted_at', 'updated_at')
    date_hierarchy = 'posted_at'

