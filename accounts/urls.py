from django.urls import path
from . import views, admin_views

app_name = 'accounts'

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('profile/', views.profile, name='profile'),
    path('profile/edit/', views.profile_edit, name='profile_edit'),
    path('dashboard/', views.job_seeker_dashboard, name='job_seeker_dashboard'),
    
    path('admin/dashboard/', admin_views.admin_dashboard, name='admin_dashboard'),
    path('admin/users/', admin_views.manage_users, name='manage_users'),
    path('admin/users/add/', admin_views.add_user, name='add_user'),
    path('admin/users/<int:pk>/edit/', admin_views.edit_user, name='edit_user'),
    path('admin/users/<int:pk>/delete/', admin_views.delete_user, name='delete_user'),
    path('admin/users/<int:pk>/toggle-status/', admin_views.toggle_user_status, name='toggle_user_status'),
    
    path('admin/companies/', admin_views.manage_companies, name='manage_companies'),
    path('admin/companies/<int:pk>/edit/', admin_views.edit_company, name='edit_company'),
    path('admin/companies/<int:pk>/delete/', admin_views.delete_company, name='delete_company'),
    path('admin/companies/<int:pk>/toggle-verification/', admin_views.toggle_company_verification, name='toggle_company_verification'),
]
