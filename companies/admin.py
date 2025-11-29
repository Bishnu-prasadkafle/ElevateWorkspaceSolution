from django.contrib import admin
from .models import Company


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('company_name', 'industry', 'location', 'verified', 'status', 'created_at')
    list_filter = ('status', 'verified', 'industry', 'created_at')
    search_fields = ('company_name', 'industry', 'location')
    fieldsets = (
        ('User Account', {'fields': ('user',)}),
        ('Company Information', {'fields': ('company_name', 'industry', 'company_size')}),
        ('Location & Web', {'fields': ('location', 'website')}),
        ('Description', {'fields': ('description',)}),
        ('Media', {'fields': ('logo',)}),
        ('Status', {'fields': ('status', 'verified')}),
        ('Timestamps', {'fields': ('created_at', 'updated_at'), 'classes': ('collapse',)}),
    )
    readonly_fields = ('created_at', 'updated_at')

