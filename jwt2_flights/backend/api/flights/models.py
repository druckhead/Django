from django.db import models


class Flight(models.Model):
    flight_number = models.SmallIntegerField(null=False, blank=False, unique=True)

    origin_city = models.CharField(null=True, blank=True, max_length=128)
    destination_city = models.CharField(null=True, blank=True, max_length=128)

    origin_airport_code = models.CharField(null=True, blank=True, max_length=3)
    destination_airport_code = models.CharField(null=True, blank=True, max_length=3)

    date_time_origin = models.DateTimeField(null=True, blank=True)
    date_time_destination = models.DateTimeField(null=True, blank=True)

    total_num_seats = models.SmallIntegerField(null=False, blank=False)
    seats_left = models.SmallIntegerField(null=False, blank=False)

    is_cancelled = models.BooleanField(default=False)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    
    def save(self, *args, **kwargs):
        if self.seats_left is None:
            self.seats_left = self.total_num_seats
        return super().save(*args, **kwargs)

    def __str__(self) -> str:
        return f"{self.flight_number}"

    class Meta:
        db_table = "flights"
