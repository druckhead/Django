import imp
from django.contrib.auth.models import User
from django.db import models
from django_extensions.db.models import TimeStampedModel
from django.core.exceptions import ValidationError

from ..flights.models import Flight


class Order(TimeStampedModel, models.Model):
    flight = models.ForeignKey(
        to=Flight,
        on_delete=models.DO_NOTHING,
    )
    user = models.ForeignKey(
        to=User,
        on_delete=models.DO_NOTHING,
    )
    number_of_seats = models.SmallIntegerField()
    total_price = models.DecimalField(max_digits=8, decimal_places=2)

    def clean(self) -> ValidationError | None:
        if self.number_of_seats > self.flight.seats_left:
            raise ValidationError(
                {
                    "seats": "Number of ordered seats can not exceed number of seats left on flight"
                }
            )

    def __str__(self) -> str:
        return f"{self.flight_id}"

    class Meta:
        db_table = "orders"
