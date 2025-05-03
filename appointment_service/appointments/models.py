from django.db import models
from django.contrib.auth.models import User
from managers import AppointmentQuerySet


class Appointment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    status = models.CharField(max_length=20, choices=[
        ('pending', 'Pending'),
        ('confirmed', 'Confirmed'),
        ('cancelled', 'Cancelled')
    ])
    created_at = models.DateTimeField(auto_now_add=True)

    objects = AppointmentQuerySet.as_manager()
    
    def __str__(self):
        return f"{self.user.username} - {self.date} {self.time}"