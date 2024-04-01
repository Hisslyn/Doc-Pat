from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import time
from django.conf import settings

class CustomUser(AbstractUser):
    # Add any additional fields here
    pass

class TimeSlot(models.Model):
    slot_time = models.TimeField(unique=True)
    is_available = models.BooleanField(default=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"{self.slot_time} - {'Available' if self.is_available else 'Booked'}"

    @property
    def display_time(self):
        return self.slot_time.strftime('%H:%M')

        
class Doctor(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    profession = models.CharField(max_length=100)
    
    def __str__(self):
        return f"{self.name} {self.surname} - {self.profession}"
    
    available_slots = models.ManyToManyField(TimeSlot, blank=False)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)  # Call the "real" save method.
        # Associate all TimeSlot instances with this Doctor
        all_slots = TimeSlot.objects.all()
        self.available_slots.set(all_slots)
        
    def __str__(self):
        return f"Dr. {self.name} {self.surname}"
    
class Appointment(models.Model):
    patient = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    doctor = models.ForeignKey('Doctor', on_delete=models.CASCADE)
    time_slot = models.ForeignKey('TimeSlot', on_delete=models.CASCADE)
    status = models.CharField(max_length=10, choices=[('pending', 'Pending'), ('confirmed', 'Confirmed'), ('cancelled', 'Cancelled')])
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.patient}'s appointment with {self.doctor} on {self.time_slot}"