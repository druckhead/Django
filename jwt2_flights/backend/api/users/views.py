from django.contrib.auth.models import User
from rest_framework import viewsets

from .serializers import UserResgisterSerializer, UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()