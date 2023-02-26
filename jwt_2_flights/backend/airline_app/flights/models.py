from django.db import models

class Flight(models.Model):
    flight_number = models.SmallIntegerField()

    origin_city = models.CharField(max_length=50)
    destination_city = models.CharField(max_length=50)

    origin_airport_code = models.CharField(max_length=3)
    destination_airport_code = models.CharField(max_length=3)

    date_time_origin = models.DateTimeField()
    date_time_destination = models.DateTimeField()

    total_num_seats = models.SmallIntegerField()
    seats_left = models.SmallIntegerField()

    is_cancelled = models.BooleanField(default=False)
    price = models.FloatField()

    def __str__(self) -> str:
        return f"{self.flight_number}"

    class Meta:
        db_table = "flights"


