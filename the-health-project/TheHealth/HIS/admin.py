from django.contrib import admin
from .models import CreateID,Patient, Doctor
# Register your models here.

admin.site.register(Patient)
admin.site.register(Doctor)
admin.site.register(CreateID)