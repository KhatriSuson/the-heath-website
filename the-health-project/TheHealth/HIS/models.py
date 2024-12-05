from pyclbr import Class
from django.db import models

# Create your models here.
Class CreateId(models.Model):
    irstName = models.CharField(max_length=100)
    MiddleName = models.CharField(max_length=100)
    SureName = models.CharField(max_length=100)
    DateOfBirth = models.DateField()
    Age = models.IntegerField()
    Sex = models.CharField(max_length=10)
    District = models.CharField(max_length=100)
    LocalLevel = models.CharField(max_length=100)
    Ward = models.CharField(max_length=100)
    Tole = models.CharField(max_length=100)
    MobileNumber = models.IntegerField()
    NameOfGuardian = models.CharField(max_length=100)
    MobileNumberOfGuardian = models.IntegerField()


    def __str__(self):
        return self.FirstName

Class Patient(models.Model):
    PatientID = models.ForeignKey(CreateId, on_delete=models.CASCADE)
    BloodGroup = models.CharField(max_length=10)
    Height = models.FloatField()
    Weight = models.FloatField()
    Allergies = models.CharField(max_length=100)
    ChronicDiseases = models.CharField(max_length=100)
    EmergencyContact = models.IntegerField()
    EmergencyContactName = models.CharField(max_length=100)
    EmergencyContactRelationship = models.CharField(max_length=100)
    EmergencyContactAddress = models.CharField(max_length=100)
    EmergencyContactMobile = models.IntegerField()

    def __str__(self):
        return self.PatientID.FirstName
    
Class Doctor(models.Model):
    DoctorID = models.ForeignKey(CreateId, on_delete=models.CASCADE)
    Specialization = models.CharField(max_length=100)
    Department = models.CharField(max_length=100)
    Qualification = models.CharField(max_length=100)
    Experience = models.IntegerField()
    ConsultationFee = models.IntegerField()

    def __str__(self):
        return self.DoctorID.FirstName
    
Class Appointment(models.Model):
    PatientID = models.ForeignKey(Patient, on_delete=models.CASCADE)
    DoctorID = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    Date = models.DateField()
    Time = models.TimeField()
    Status = models.CharField(max_length=100)

    def __str__(self):
        return self.PatientID.PatientID.FirstName

Class Prescription(models.Model):
    AppointmentID = models.ForeignKey(Appointment, on_delete=models.CASCADE)
    Medicine = models.CharField(max_length=100)
    Dosage = models.CharField(max_length=100)
    Frequency = models.CharField(max_length=100)
    Duration = models.CharField(max_length=100)

    def __str__(self):
        return self.AppointmentID.PatientID.PatientID.FirstName