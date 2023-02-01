import os
import django

os.environ["DJANGO_SETTINGS_MODULE"] = "movies.settings"
django.setup()

from movies_app.models import *
from datetime import datetime
from django.db.models import Q, Count, Min, Max, Avg, Sum
from django.db.models.functions import Round


def one():
    actors = Actor.objects.filter(birth_year__gte=datetime.now().year - 50)
    return actors


def two():
    movies = Movie.objects.filter(duration_in_min__lt=150, release_year__gt=2005)
    return movies


def three():
    movies = Movie.objects.filter(
        Q(description__contains="criminal")
        | Q(description__contains="mob")
        | Q(description__contains="cop")
    )
    return movies


def four():
    movies = three().filter(release_year__lt=2010)
    return movies


def five():
    actors = Actor.objects.annotate(num_movies=Count("movie", distinct=True))
    return actors


def six():
    movies = Rating.objects.aggregate(Max("rating"), Min("rating"), Avg("rating"))
    return movies


def seven():
    movies = Movie.objects.annotate(
        avg_rating=Round(Avg("rating__rating"), precision=2)
    )
    return movies


def eight():
    ratings = Rating.objects.filter(rating_date__year=2023)
    return ratings


def nine():
    actors = Actor.objects.annotate(
        max_rating=Max("movie__rating__rating"), min_rating=Min("movie__rating__rating")
    )
    return actors


def ten():
    movies = Movie.objects.annotate(avg_actor_salary=Avg("movieactor__salary"))
    return movies


def eleven():
    actors = Actor.objects.annotate(total_salary=Sum("movieactor__salary"))
    return actors


def twelve():
    actors = Actor.objects.annotate(atleast_once=Count("movieactor__main_role")).filter(
        atleast_once__gte=1
    )
    return actors


def thirteen():
    movies = Movie.objects.filter(movieactor__main_role=True).annotate(
        actors_in_main_roles=Count("movieactor__main_role")
    )
    return movies
