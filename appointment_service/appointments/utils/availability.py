from appointments.services import AvailabilityService

def get_available_slots(date, start_time="09:00", end_time="18:00", interval_minutes=30):
    """
    Returns a list of available slots for a given date.
    """
    return AvailabilityService.get_available_slots(date, start_time, end_time, interval_minutes)