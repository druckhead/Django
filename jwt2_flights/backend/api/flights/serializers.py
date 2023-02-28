from rest_framework import serializers

from .models import Flight

class FlightSerializer(serializers.ModelSerializer):
    model = Flight
    fields = "__all__"