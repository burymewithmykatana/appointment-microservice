from rest_framework.throttling import UserRateThrottle

class AppointmentRateThrottle(UserRateThrottle):
    rate = '5/hour'  # Limit to 5 requests per hour per user