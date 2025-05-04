from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
import uuid


class MyUserManager(BaseUserManager):
    def create_user(self, phone_number, password=None, **extra_fields):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not phone_number:
            raise ValueError("Users must have an phone number")

        user = self.model(
            phone_number=phone_number,
            **extra_fields,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, phone_number, password=None, **extra_fields):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(
            phone_number=phone_number,
            password=password,
            **extra_fields

        )
        user.is_admin = True
        user.is_active = True
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user


class Customuser(AbstractBaseUser):

    phone_number = models.CharField(max_length=50, unique=True)
    first_name = models.CharField(max_length=50)
    is_superuser = models.BooleanField(default=False)
    is_patient = models.BooleanField(default=False)
    is_doctor =  models.BooleanField(default=False)
    role = models.CharField(max_length=50)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = MyUserManager()

    USERNAME_FIELD = "phone_number"
    REQUIRED_FIELDS = ["first_name"]

    def __str__(self):
        return self.first_name

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return self.is_superuser

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return self.is_superuser


class DoctorProfile(models.Model):
    user = models.OneToOneField(Customuser, on_delete=models.CASCADE)
    department = models.CharField(max_length=100)
    specialization = models.TextField()

    def __str__(self):
        return self.user.first_name

class PatientProfile(models.Model):
    user = models.OneToOneField(Customuser, on_delete=models.CASCADE)
    age = models.IntegerField()
    address = models.TextField()

    def __str__(self):
        return self.user.first_name

class Appointment(models.Model):
    patient = models.ForeignKey(Customuser, on_delete=models.CASCADE, related_name='patient_appointments')
    doctor = models.ForeignKey(Customuser, on_delete=models.CASCADE, related_name='doctor_appointments')
    appointment_date = models.DateField()
    description = models.TextField()
    is_approved = models.BooleanField(default=False)

    def __str__(self):
        return f" Appointment of {self.patient.first_name} with {self.doctor.first_name} on {self.appointment_date}"
