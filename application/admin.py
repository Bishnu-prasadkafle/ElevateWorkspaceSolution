from django.contrib import admin
from .models import JobApplication


@admin.register(JobApplication)
class JobApplicationAdmin(admin.ModelAdmin):
    list_display = ('job_seeker', 'job', 'status', 'applied_at')
    list_filter = ('status', 'applied_at', 'job__company')
    search_fields = ('job_seeker__user__username', 'job__title', 'job__company__company_name')
    fieldsets = (
        ('Application Info', {'fields': ('job_seeker', 'job')}),
        ('Application Status', {'fields': ('status',)}),
        ('Cover Letter', {'fields': ('cover_letter',)}),
        ('Timestamps', {'fields': ('applied_at', 'updated_at'), 'classes': ('collapse',)}),
    )
    readonly_fields = ('applied_at', 'updated_at')
    date_hierarchy = 'applied_at'

