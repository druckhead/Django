from django.contrib.auth.models import User
from django.db import models
from django_extensions.db.models import TimeStampedModel


class Order(TimeStampedModel, models.Model):
    flight = models.ForeignKey(
        to="flights.Flight",
        on_delete=models.CASCADE,
    )
    user = models.ForeignKey(
        to=User,
        on_delete=models.DO_NOTHING,
    )
    number_of_seats = models.SmallIntegerField()
    total_price = models.FloatField()

    def __str__(self) -> str:
        return f"{self.flight_id}"

    class Meta:
        db_table = "orders"
