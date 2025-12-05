from django.contrib import admin
from django.utils.html import format_html
from django.utils.safestring import mark_safe
from .models import JobApplication, ApplicationDocument


@admin.register(JobApplication)
class JobApplicationAdmin(admin.ModelAdmin):
    list_display = ('job_seeker', 'job', 'status', 'applied_at', 'resume_link')
    list_filter = ('status', 'applied_at', 'job__company')
    search_fields = ('job_seeker__user__username', 'job__title', 'job__company__company_name')
    fieldsets = (
        ('Application Info', {'fields': ('job_seeker', 'job')}),
        ('Application Status', {'fields': ('status',)}),
        ('Cover Letter', {'fields': ('cover_letter',)}),
        ('Files', {'fields': ('resume',)}),
        ('Timestamps', {'fields': ('applied_at', 'updated_at'), 'classes': ('collapse',)}),
    )
    readonly_fields = ('applied_at', 'updated_at')
    date_hierarchy = 'applied_at'

    def resume_link(self, obj):
        if obj.resume:
            return format_html('<a href="{}" target="_blank" rel="noopener">Download</a>', obj.resume.url)
        return '-'
    resume_link.short_description = 'Resume'

    def documents_list(self, obj):
        docs = obj.documents.all()
        if not docs:
            return '-'
        links = []
        for d in docs:
            name = d.label or d.file.name.split('/')[-1]
            links.append(format_html('<a href="{}" target="_blank" rel="noopener">{}</a>', d.file.url, name))
        return mark_safe(', '.join(links))
    documents_list.short_description = 'Other Documents'


@admin.register(ApplicationDocument)
class ApplicationDocumentAdmin(admin.ModelAdmin):
    list_display = ('application', 'label', 'file_link', 'uploaded_at')
    search_fields = ('application__job__title', 'label')
    readonly_fields = ('uploaded_at',)

    def file_link(self, obj):
        if obj.file:
            return format_html('<a href="{}" target="_blank" rel="noopener">Download</a>', obj.file.url)
        return '-'
    file_link.short_description = 'File'

