from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import time
from django.conf import settings

class CustomUser(AbstractUser):
    # Add any additional fields here
    pass

class TimeSlot(models.Model):
    slot_time = models.TimeField(unique=True)

    def __str__(self):
        return f"{self.slot_time.strftime('%H:%M')}"

    class Meta:
        ordering = ['slot_time']

        
class Doctor(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    profession = models.CharField(max_length=100)

    TIME_SLOTS = (
    ('09:00', '09:30'),
    ('09:30', '10:00'),
    ('10:00', '10:30'),
    ('10:30', '11:00'),
    ('11:00', '11:30'),
    ('11:30', '12:00'),
    ('12:00', '12:30'),
    ('12:30', '13:00'),
    ('13:00', '13:30'),
    ('13:30', '14:00'),
    ('14:00', '14:30'),
    ('14:30', '15:00'),
    ('15:00', '15:30'),
    ('15:30', '16:00'),
    ('16:00', '16:30'),
    ('16:30', '17:00'),
    ('17:00', '17:30'),
    ('17:30', '18:00'),
)

    
    def __str__(self):
        return f"{self.name} {self.surname} - {self.profession}"
    
    available_slots = models.ManyToManyField(TIME_SLOTS, blank=True)

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