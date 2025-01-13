from pyclbr import Class
from django.db import models
# Create your models here.
class CreateID(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    address = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    email = models.EmailField()
    disease = models.CharField(max_length=100)
    date = models.DateField()
    time = models.TimeField()
    doctor = models.CharField(max_length=100)
    status = models.CharField(max_length=100)
    prescription = models.CharField(max_length=100)
    report = models.CharField(max_length=100)
    def __str__(self):
        return self.name
    
class Patient(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    address = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    email = models.EmailField()
    disease = models.CharField(max_length=100)
    date = models.DateField()
    time = models.TimeField()
    doctor = models.CharField(max_length=100)
    status = models.CharField(max_length=100)
    prescription = models.CharField(max_length=100)
    report = models.CharField(max_length=100)
    def __str__(self):
        return self.name
    
class Doctor(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    address = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    email = models.EmailField()
    department = models.CharField(max_length=100)
    def __str__(self):
        return self.name