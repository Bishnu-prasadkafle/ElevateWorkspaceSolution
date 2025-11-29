from django.urls import path
from . import views

app_name = 'application'

urlpatterns = [
    path('apply/<int:job_id>/', views.apply_job, name='apply_job'),
    path('<int:pk>/', views.application_detail, name='application_detail'),
    path('my-applications/', views.my_applications, name='my_applications'),
    path('<int:pk>/withdraw/', views.withdraw_application, name='withdraw_application'),
    path('<int:pk>/update-status/', views.update_application_status, name='update_application_status'),
    path('company/dashboard/', views.company_dashboard, name='company_dashboard'),
]
