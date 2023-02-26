from django.urls import include, path


urlpatterns = [
    path("flights/", include("airline_app.flights.urls")),
    path("orders/", include("airline_app.orders.urls")),
    path("users/", include("airline_app.users.urls")),
]