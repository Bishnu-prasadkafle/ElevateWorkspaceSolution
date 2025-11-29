from django.contrib import admin
from .models import User, JobSeeker


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'role', 'is_active', 'created_at')
    list_filter = ('role', 'is_active', 'created_at')
    search_fields = ('username', 'email', 'first_name', 'last_name')
    fieldsets = (
        ('User Information', {'fields': ('username', 'email', 'first_name', 'last_name')}),
        ('Role & Contact', {'fields': ('role', 'phone_number')}),
        ('Status', {'fields': ('is_active', 'is_staff', 'is_superuser')}),
        ('Dates', {'fields': ('created_at', 'updated_at'), 'classes': ('collapse',)}),
    )
    readonly_fields = ('created_at', 'updated_at')


@admin.register(JobSeeker)
class JobSeekerAdmin(admin.ModelAdmin):
    list_display = ('user', 'location', 'experience_years', 'created_at')
    list_filter = ('experience_years', 'location', 'created_at')
    search_fields = ('user__username', 'user__email', 'location')
    fieldsets = (
        ('User Profile', {'fields': ('user',)}),
        ('Professional Info', {'fields': ('bio', 'skills', 'experience_years')}),
        ('Contact', {'fields': ('location',)}),
        ('Media', {'fields': ('profile_picture', 'resume')}),
    )

