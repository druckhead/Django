from django.urls import path

from . import views

urlpatterns = [
    path("api/movies", views.movies_list),
    path("api/movies/<int:movie_id>", views.movie_details),
    path("api/movies/<int:movie_id>/actors", views.movie_actors),
    path("api/ratings", views.ratings_list),
    path("", views.index),
]
