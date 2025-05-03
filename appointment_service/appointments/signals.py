from django.db.models.signals import post_save
from django.dispatch import receiver
from appointments.models import Appointment
from appointments.services import NotificationService

@receiver(post_save, sender=Appointment)
def send_appointment_notification(sender, instance, created, **kwargs):
    if created:
        NotificationService.send_email_notification.delay(
            instance.user.email,
            f"Your appointment on {instance.date} at {instance.time} is confirmed."
        )