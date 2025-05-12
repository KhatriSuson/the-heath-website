from django.dispatch import Signal
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.contrib.auth.signals import user_logged_in
from accounts.models import *


@receiver(post_save, sender =Customuser )
def automatic_create_a_doctor_profile(sender, instance, created, **kwargs):
    if created:
            if instance.is_doctor:
                DoctorProfile.objects.get_or_create(user=instance)
                print('profile is created ')

            elif instance.is_patient:
                PatientProfile.objects.get_or_create(user = instance)
                print('profile is created patient')


        
