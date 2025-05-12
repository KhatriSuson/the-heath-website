from typing import Any, Dict, Optional
from django import http
from django.db import models
from django.db.models.query import QuerySet
from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.http.response import HttpResponse
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




def home(request):
    return render(request, 'accounts/home.html')



# doctor  view
class Doctorview(FormView):
    form_class = DoctorRegistration
    template_name = 'accounts/doctor_registration.html'
    success_url = reverse_lazy('doctor_login')


    def form_valid(self, form):
        user = form.save(commit= False)
        user.role = 'doctor'
        user.is_doctor = True
        user.save()
        return super().form_valid(form)
    




def success(request):
   
    return HttpResponse('success')



class Doctor_login_view(LoginView):
    template_name = 'accounts/doctor_login.html'
    authentication_form = DoctorLoginForm

    def get_success_url(self):
        return reverse_lazy('doctor_dash')



class doctordashboardview(IsDoctorMixin, ListView):
    template_name = 'accounts/doctor_dashboard.html'
    model = Appointment

    def get_queryset(self):
        return Appointment.objects.select_related('doctor').filter(doctor = self.request.user).order_by('-appointment_date')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        today = timezone.localdate()
        context['date_today'] = today
        context['today_count'] = Appointment.objects.filter(doctor=self.request.user, appointment_date=today)
        context['approve_appointment'] = Appointment.objects.filter(doctor=self.request.user,is_approved = True).count()
        context['doctorprofile'] = self.request.user.doctorprofile
        return context
    
    

class doctorlogoutview(IsDoctorMixin,View):
    def get(self, request):
        logout(request)
        return redirect('doctor_login')
    


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


class DoctorProfileUpdatevIEW(LoginRequiredMixin,UpdateView):
    model = DoctorProfile
    form_class = DoctorprofileForm
    template_name = 'accounts/edit_profile.html'

    def get_success_url(self):
        return reverse_lazy('doctor_dash')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['doctorprofile'] = self.request.user.doctorprofile

      
    

class ReportView(LoginRequiredMixin, CreateView):
    template_name = 'accounts/report.html'
    form_class = reportform

    def get_success_url(self):
        return reverse_lazy('doctor_dash')
    
    def dispatch(self, request, *args, **kwargs):
        self.appointment = get_object_or_404(Appointment, pk = self.kwargs['pk'])
        print(self.appointment.patient)
        if self.appointment.doctor != self.request.user:
            return self.handle_no_permission()

        return super().dispatch(request, *args, **kwargs)
    
    def form_valid(self, form):
            doctor_profile = DoctorProfile.objects.get(user=self.request.user)
            patient_profile = PatientProfile.objects.get(user=self.appointment.patient)

            form.instance.doctorprofile = doctor_profile
            form.instance.patientprofle = patient_profile
            form.instance.report_date = timezone.now().date()
            return super().form_valid(form)
            

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['appointment'] = self.appointment
        return context
    

    # for checking the reports


    
