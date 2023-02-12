from django.shortcuts import get_object_or_404, render
from django.urls import is_valid_path
from movies_app.models import *
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response

from .serializers import *


# Create your views here.
def get_movies_list(request: Request):
    movies_qs = Movie.objects.all()
    if "name" in request.query_params:
        movies_qs = movies_qs.filter(name__iexact=request.query_params["name"])
    if "duration_from" in request.query_params:
        movies_qs = movies_qs.filter(
            duration_in_min__gte=request.query_params["duration_from"]
        )
    if "duration_to" in request.query_params:
        movies_qs = movies_qs.filter(
            duration_in_min__lte=request.query_params["duration_to"]
        )
    if "description" in request.query_params:
        movies_qs = movies_qs.filter(
            description__icontains=request.query_params["description"]
        )

    if not movies_qs:
        return Response(status=status.HTTP_204_NO_CONTENT)

    serializer = MovieSerializer(movies_qs, many=True)
    return Response(serializer.data)


@api_view(["GET", "POST"])
def movies_list(request: Request):
    if request.method == "GET":
        return get_movies_list(request)
    elif request.method == "POST":
        serializer = MovieDetailsSerializer(data=request.data)  # type: ignore
        if serializer.is_valid(raise_exception=True):
            serializer.create(serializer.validated_data)
            return Response(status=status.HTTP_201_CREATED)


@api_view(["GET", "PATCH", "DELETE"])
def movie_details(request: Request, movie_id: int):
    movie = get_object_or_404(Movie, id=movie_id)
    if request.method == "GET":
        serializer = MovieDetailsSerializer(movie, many=False)
        return Response(serializer.data)
    elif request.method == "PATCH":
        serializer = MovieDetailsSerializer(
            movie,
            data=request.data,  # type: ignore
            many=False,
            partial=True,
        )
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(status=status.HTTP_200_OK)
    elif request.method == "DELETE":
        movie.delete()
        return Response(status=status.HTTP_200_OK)


@api_view(["GET"])
def ratings_list(request: Request):
    ratings_qs = Rating.objects.all()

    if (
        "rating" in request.query_params
        and ("rating_from" or "rating_to") in request.query_params
    ):
        return Response(status=status.HTTP_400_BAD_REQUEST)

    if "rating" in request.query_params:
        ratings_qs = ratings_qs.filter(rating=request.query_params["rating"])
    else:
        if "rating_from" in request.query_params:
            ratings_qs = ratings_qs.filter(
                rating__gte=request.query_params["rating_from"]
            )
        if "rating_to" in request.query_params:
            ratings_qs = ratings_qs.filter(
                rating__lte=request.query_params["rating_to"]
            )

    if (
        "date" in request.query_params
        and ("date_from" or "date_to") in request.query_params
    ):
        return Response(status=status.HTTP_400_BAD_REQUEST)

    if "date" in request.query_params:
        ratings_qs = ratings_qs.filter(rating_date=request.query_params["date"])
    else:
        if "date_from" in request.query_params:
            ratings_qs = ratings_qs.filter(
                rating_date__gte=request.query_params["date_from"]
            )
        if "date_to" in request.query_params:
            ratings_qs = ratings_qs.filter(
                rating_date__lte=request.query_params["date_to"]
            )

    if not ratings_qs:
        return Response(status=status.HTTP_204_NO_CONTENT)

    serializer = RatingSerializer(ratings_qs, many=True)
    return Response(serializer.data)


@api_view(["GET", "POST"])
def movie_actors(request: Request, movie_id: int):
    if request.method == "GET":
        movie_actors = MovieActor.objects.filter(movie_id=movie_id)
        if 'main_roles' in request.query_params:
            is_true = request.query_params['main_roles'] == '1'
            if is_true:
                movie_actors = movie_actors.filter(main_role=True)
        if 'salary_from' in request.query_params:
            movie_actors = movie_actors.filter(salary__gte=request.query_params['salary_from'])
        if 'salary_to' in request.query_params:
            movie_actors = movie_actors.filter(salary__lte=request.query_params['salary_to'])
        serializer = MovieActorSerializer(movie_actors, many=True)
        return Response(serializer.data)
    elif request.method == "POST":
        movie = get_object_or_404(Movie, id=movie_id)
        serializer = AddMovieActorSerializer(
            data=request.data,  # type: ignore
            context={"movie_id": movie_id, "request": request},
        )
        if serializer.is_valid(raise_exception=True):
            serializer.create(serializer.validated_data)
            return Response(status=status.HTTP_200_OK)


def index(request):
    return render(request, "index.html")
