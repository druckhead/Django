from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication

from ..models import Movie, Review


@api_view(["GET"])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated, IsAdminUser])
def stats(request):
    users = User.objects.all().count()
    movies = Movie.objects.all().count()
    reviews = Review.objects.all().count()

    stats_json = {
        "total_users": users,
        "total_movies": movies,
        "reviews": reviews
    }

    return Response(stats_json, status=status.HTTP_200_OK)
