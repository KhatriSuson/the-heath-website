from django.contrib import admin
from .models import CreateID Patient, Doctor, Appointment, Prescription, Test, TestResult, Payment, PaymentMethod, Insurance, InsuranceProvider, InsuranceCoverage, InsurancePayment, InsurancePaymentMethod, InsurancePaymentCoverage, InsurancePaymentCoverageMethod, InsurancePaymentCoverageMethodPayment
# Register your models here.

admin.site.register(CreateID)