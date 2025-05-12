from typing import Any, Dict, Optional
from django.db import models
from django.db.models.query import QuerySet
from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.views.generic.edit import FormView
from accounts.forms import *
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.views import View
from django.contrib.auth import logout
from accounts.mixins import *
from django.views.generic import CreateView,ListView,DeleteView,DetailView,UpdateView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils import timezone
from django.shortcuts import get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.core.exceptions import PermissionDenied
from accounts.views.patient_views import *
from accounts.models import *
from django.views.generic import TemplateView
from django.utils.decorators import method_decorator





def home(request):
    return render(request, 'accounts/home.html')




class Patientview(FormView):
    form_class = PatientRegistration
    template_name = 'accounts/patient_registration.html'
    success_url = reverse_lazy('patient_login')


    def form_valid(self, form):
        user = form.save(commit= False)
        user.role = 'patient'
        user.is_patient = True
        user.save()
        return super().form_valid(form)
    



def success(request):
    return HttpResponse('success')


class Patient_login_view(LoginView):
    template_name = 'accounts/patient_login.html'
    authentication_form = patientLoginForm

    def get_success_url(self):
        return reverse_lazy('patient_dashboard')



class patientdashboardview(IsPatientMixin, ListView):
    model = Appointment
    template_name = 'accounts/patient_dashboard.html'

    def get_queryset(self):
        return Appointment.objects.filter(patient = self.request.user)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['patient_report'] = Report.objects.select_related('patientprofle').filter(patientprofle__user = self.request.user)
        return context
    
    

class patientlogoutview(IsPatientMixin,View):
    def get(self, request):
        logout(request)
        return redirect('home')


class PatientAppointmentvIEW(LoginRequiredMixin,CreateView):
    login_url = 'patient_login'
    model = Appointment
    form_class = AppointForm
    template_name = 'accounts/patient_appoint.html'

    def get_success_url(self):
        return reverse_lazy('patient_dashboard')

    def form_valid(self, form):
        doctor = form.cleaned_data['doctor']
        appointment_date  = form.cleaned_data['appointment_date']

        existing_appoinment = Appointment.objects.filter(doctor = doctor, appointment_date = appointment_date)

        if existing_appoinment.exists():
            form.add_error('appointment_date', 'The doctor is already booked in this date and time choose another')
            return self.form_invalid(form)
        
        appoinment = form.save(commit=False)
        appoinment.patient = self.request.user
        appoinment.is_approved = False
        appoinment.save()
        return super().form_valid(form)
    

class PatientDetails(DetailView):
    template_name = 'accounts/patient_profile.html'
    model = PatientProfile
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["profile"] = PatientProfile.objects.all()
        return context




class approveappoint(LoginRequiredMixin, View):
    def get(self, request, pk, *args, **kwargs):
        appointment = get_object_or_404(Appointment, pk=pk, doctor = self.request.user)
        appointment.is_approved = True
        appointment.save()
        return redirect('doctor_dash')



    
class AppointDeleteView(DeleteView):
    model = Appointment
    success_url = reverse_lazy("doctor_dash")
    template_name = 'accounts/appointment_confirm.html'




class PatientDetailsView(LoginRequiredMixin, DetailView):
    model = PatientProfile
    context_object_name = 'patient'
   
    # def get_object(self):
    #     patient =  super().get_object()
    #     if patient.doctorprofile != self.request.user.doctorprofile:
    #         raise PermissionDenied('तपाईंलाई यस बिरामीको प्रोफाइल हेर्न अनुमति छैन।')
    #     return patient
    
    
    

class DoctorDetailsView(DetailView):
    model = DoctorProfile
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
    
# views.py
@method_decorator(login_required, name='dispatch')
class ServiceDetailView(TemplateView):
    template_name = 'services/default.html'  # fallback

    def get_template_names(self):
        service_slug = self.kwargs.get('service_slug')

        # Try loading service-specific template
        possible_template = f'services/{service_slug}.html'
        
        # You can optionally verify if the template exists
        from django.template.loader import get_template
        try:
            get_template(possible_template)
            return [possible_template]
        except:
            return ['services/404.html']  # or default.html

class allservicesview(View):
    def get(request, self, *args, **kwargs):
        return render(request, 'services/allservices.html')