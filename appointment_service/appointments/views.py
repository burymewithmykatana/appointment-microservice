from rest_framework.viewsets import ModelViewSet
from rest_framework.exceptions import ValidationError
from appointments.services import AvailabilityService
from throttles import AppointmentRateThrottle


class AppointmentViewSet(ModelViewSet):
    
    throttle_classes = [AppointmentRateThrottle]
    def create(self, request, *args, **kwargs):
        date = request.data['date']
        time = request.data['time']
        if not AvailabilityService.is_slot_available(date, time):
            raise ValidationError("The selected time slot is not available.")

        return super().create(request, *args, **kwargs)