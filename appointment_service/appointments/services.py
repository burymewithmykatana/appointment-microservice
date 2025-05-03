from appointments.models import Appointment
from celery import shared_task


# this service is used in parts of the system where availability checks are required.
class AvailabilityService:
    @staticmethod
    def is_slot_available(date, time):
        """
        Checks if a given date and time slot is available for booking.
        """
        return not Appointment.objects.filter(date=date, time=time).exists()
    

class NotificationService:
    @staticmethod
    @shared_task
    def send_email_notification(user_email, message):
        """
        Sends an email notification to the user.
        """
        # an email-sending library
        from django.core.mail import send_mail
        send_mail(
            'Appointment Notification',
            message,
            'no-reply@example.com',
            [user_email],
        )