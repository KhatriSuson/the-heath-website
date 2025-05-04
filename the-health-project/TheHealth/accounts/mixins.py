from typing import Optional
from django.contrib.auth.mixins import UserPassesTestMixin
from django.http import HttpResponseForbidden
from django.http.response import HttpResponseRedirect
from django.urls import reverse_lazy
from django.shortcuts import render





class IsDoctorMixin(UserPassesTestMixin):
    login_url = 'doctor_login'
    def test_func(self):
        return self.request.user.is_authenticated and hasattr(self.request.user, 'is_doctor') and self.request.user.is_doctor
    
    def handle_no_permission(self):
        if self.request.user.is_authenticated:
                return render(self.request, 'accounts/403.html')
        return super().handle_no_permission()

        
    
class IsPatientMixin(UserPassesTestMixin):
    login_url = 'patient_login'
    def test_func(self):
        return self.request.user.is_authenticated and hasattr(self.request.user, 'is_patient') and self.request.user.is_patient
    
    def handle_no_permission(self):
        if self.request.user.is_authenticated:
            return render(self.request, 'accounts/403.html')
        return super().handle_no_permission()