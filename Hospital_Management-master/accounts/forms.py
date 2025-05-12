from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from accounts.models import *


class DoctorRegistration(UserCreationForm):
    class Meta:
        model = Customuser
        fields = ['phone_number', 'first_name', 'password1', 'password2']




class DoctorLoginForm(AuthenticationForm):
    class Meta:
        model = Customuser
        fields = ['username', 'password']






class PatientRegistration(UserCreationForm):
    class Meta:
        model = Customuser
        fields = ['phone_number', 'first_name', 'password1', 'password2']



class patientLoginForm(AuthenticationForm):
    class Meta:
        model = Customuser
        fields = ['username', 'password']


# appointment form
class AppointForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['doctor', 'appointment_date', 'description']
        widgets = {
            'appointment_date': forms.DateInput(attrs={'type': 'date'})
        }

    def __init__(self, *args, **kwargs):
        super(AppointForm, self).__init__(*args, **kwargs)
        self.fields['doctor'].queryset = Customuser.objects.filter(is_doctor=True)

            
# doctor profile form
class DoctorprofileForm(forms.ModelForm):
    class Meta:
        model = DoctorProfile
        fields = ['department', 'specialization']




class reportform(forms.ModelForm):
    class Meta:
        model = Report
        fields = ['report_result', 'report_date', 'report_images']
