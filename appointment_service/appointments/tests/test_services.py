from django.test import TestCase
from appointments.services import AvailabilityService
from appointments.models import Appointment

class AvailabilityServiceTest(TestCase):
    def test_is_slot_available(self):
        # Create test appointments
        Appointment.objects.create(date="2025-05-10", time="10:00:00", status="confirmed")
        
        # Test available slots
        self.assertFalse(AvailabilityService.is_slot_available("2025-05-10", "10:00:00"))
        self.assertTrue(AvailabilityService.is_slot_available("2025-05-10", "11:00:00"))