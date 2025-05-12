from django.contrib import admin
from accounts.models import *

class Useradmin(admin.ModelAdmin):
    list_display = ['phone_number', 'first_name','is_active', 'is_patient', 'is_doctor', 'role', 'is_superuser', 'is_staff']

admin.site.register(Customuser, Useradmin)


admin.site.register(Appointment)
admin.site.register(DoctorProfile)
admin.site.register(PatientProfile)
admin.site.register(Report)
