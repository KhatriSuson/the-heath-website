from typing import Any, Dict
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
from django.views.generic import CreateView,ListView,DeleteView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils import timezone
from django.shortcuts import get_object_or_404

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
    

# patience view
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



class Doctor_login_view(LoginView):
    template_name = 'accounts/doctor_login.html'
    authentication_form = DoctorLoginForm


    def get_success_url(self):
        return reverse_lazy('doctor_dash')



class doctordashboardview(IsDoctorMixin, ListView):
    template_name = 'accounts/doctor_dashboard.html'
    model = Appointment

    def get_queryset(self):
        return Appointment.objects.filter(doctor = self.request.user).order_by('-appointment_date')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        today = timezone.localdate()
        context['date_today'] = today
        context['today_count'] = Appointment.objects.filter(doctor=self.request.user, appointment_date=today)
        context['approve_appointment'] = Appointment.objects.filter(doctor=self.request.user,is_approved = True).count()
        return context
    

class doctorlogoutview(IsDoctorMixin,View):
    def get(self, request):
        logout(request)
        return redirect('doctor_login')
    

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
    


class patientlogoutview(IsPatientMixin,View):
    def get(self, request):
        logout(request)
        return redirect('patient_login')


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
    

# doctor appoinment approved


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