from django.contrib import admin

from .flights.models import Flight

@admin.register(Flight)
class FlightAdmin(admin.ModelAdmin):
    list_display = ('id', 'flight_number', 'origin_city', 'destination_city', 'origin_airport_code', 'destination_airport_code', 'date_time_origin', 'date_time_destination', 'total_num_seats', 'seats_left', 'is_cancelled', 'price')
    