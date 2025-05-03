from appointments.models import Appointment
from celery import shared_task
from datetime import datetime, timedelta
from django.core.mail import send_mail


# this service is used in parts of the system where availability checks are required.
class AvailabilityService:
    @staticmethod
    def is_slot_available(date, time):
        """
        Checks if a given date and time slot is available for booking.
        """
        return not Appointment.objects.filter(date=date, time=time).exists()

    @staticmethod
    def get_available_slots(date, start_time="09:00", end_time="18:00", interval_minutes=30):
        """
        Returns a list of available slots for a given date based on a time range and interval.
        """
        start = datetime.strptime(start_time, "%H:%M").time()
        end = datetime.strptime(end_time, "%H:%M").time()
        slots = []
        current_time = datetime.combine(date, start)

        while current_time.time() < end:
            if AvailabilityService.is_slot_available(date, current_time.time()):
                slots.append(current_time.time())
            current_time += timedelta(minutes=interval_minutes)

        return slots


class NotificationService:
    @staticmethod
    @shared_task
    def send_email_notification(user_email, subject, message):
        """
        Sends an email notification to the user.
        """
        try:
            send_mail(
                subject,
                message,
                'no-reply@example.com',
                [user_email],
            )
        except Exception as e:
            # Log the error for debugging
            print(f"Failed to send email: {e}")

    @staticmethod
    @shared_task
    def send_sms_notification(phone_number, message):
        """
        Sends an SMS notification to the user.
        (Requires integration with an SMS gateway like Twilio)
        """
        try:
            # Replace this with actual SMS sending logic
            print(f"Sending SMS to {phone_number}: {message}")
        except Exception as e:
            print(f"Failed to send SMS: {e}")


class AppointmentService:
    @staticmethod
    def cancel_appointment(appointment_id):
        """
        Cancels an appointment by ID.
        """
        appointment = Appointment.objects.get(id=appointment_id)
        appointment.is_cancelled = True
        appointment.save()


class AnalyticsService:
    @staticmethod
    def get_appointment_statistics():
        """
        Returns statistics for bookings and cancellations.
        """
        total_bookings = Appointment.objects.count()
        cancelled_bookings = Appointment.objects.filter(is_cancelled=True).count()
        return {
            "total_bookings": total_bookings,
            "cancelled_bookings": cancelled_bookings,
        }