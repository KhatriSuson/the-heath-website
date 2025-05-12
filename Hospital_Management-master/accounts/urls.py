"""
URL configuration for hospital project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from accounts.views.doctor_views import *
from accounts.views.patient_views import *


urlpatterns = [
    path('', home, name='home' ),
    path('doctor/register/', Doctorview.as_view(), name='doctor_register'),
    path('success/', success, name='success'),
    
    path('doctor/login/', Doctor_login_view.as_view(), name='doctor_login'),
    path('doctor/dashboard/', doctordashboardview.as_view(), name='doctor_dash'),
    path('doctor/logout/', doctorlogoutview.as_view(), name='doctor_logout'),

    path('doctor/approve/<pk>/', approveappoint.as_view(), name = 'approve_appointment'),

    path('appoint/delete/<int:pk>/', AppointDeleteView.as_view(), name='appoint_delete'),

    path('doctor/edit-profile/<pk>/', DoctorProfileUpdatevIEW.as_view(), name='edit_profile'),

    path('doctor-details/<pk>/', DoctorDetailsView.as_view(), name='doctor_details'),

    path('add-report/<pk>/', ReportView.as_view(), name='add_report'),


    # for the patient urls

    path('patient/register/',Patientview.as_view(), name='patient_register'),

    path('patient/login/',Patient_login_view.as_view(), name='patient_login'),

    path('patient/dashboard/',patientdashboardview.as_view(), name='patient_dashboard'),

    path('patient/logout/',patientlogoutview.as_view(), name='patient_logout'),

    path('patient/appoint/', PatientAppointmentvIEW.as_view(), name='patient_appoint'),

    path('doctor-patient/<pk>/', PatientDetailsView.as_view(template_name = 'accounts/patientprofile_detail.html'), name='view_patient_profile'),

    path('services/<slug:service_slug>/', ServiceDetailView.as_view(), name='service_detail'),

    path('services/', allservicesview.as_view(), name='all_service'),

]
