from rest_framework import status, viewsets
from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import CreateModelMixin, DestroyModelMixin, ListModelMixin, RetrieveModelMixin, UpdateModelMixin
from rest_framework.pagination import LimitOffsetPagination, PageNumberPagination
from rest_framework.permissions import IsAuthenticated, IsAdminUser, BasePermission, SAFE_METHODS
from rest_framework.response import Response

from imdb_app.models import Movie
from imdb_app.serializers.movies import MovieSerializer


class MoviesPaginationClass(PageNumberPagination):
    page_size = 3


class MoviesPermissions(BasePermission):
    def has_permission(self, request, view):
        if request.method in ['POST', 'PUT', 'PATCH']:
            return request.user.is_staff


class MoviesViewSet(CreateModelMixin,
                    RetrieveModelMixin,
                    UpdateModelMixin,
                    ListModelMixin,
                    GenericViewSet):

    queryset = Movie.objects.all()

    permission_classes = [MoviesPermissions]
    # authentication_classes = [JWTAuthentication]

    # we need different serializers for different actions
    serializer_class = MovieSerializer

    # pagination is defined either using DEFAULT_PAGINATION_CLASS in settings.py
    # or you can specify one here
    # pagination_class = MoviesPaginationClass
