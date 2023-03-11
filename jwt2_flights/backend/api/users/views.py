from django.contrib.auth.models import User
from rest_framework import generics, mixins, status, viewsets
from rest_framework.permissions import AllowAny, IsAdminUser
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.exceptions import TokenError
from rest_framework_simplejwt.tokens import RefreshToken

from .permissions import UserPermission

from .serializers import UserResgisterSerializer, UserSerializer, StaffRegisterSerializer


class UserViewSet(
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    mixins.ListModelMixin,
    viewsets.GenericViewSet,
):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [UserPermission]


class UserRegistrationViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    serializer_class = UserResgisterSerializer
    permission_classes = [AllowAny]


class StaffRegistrationViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    serializer_class = UserResgisterSerializer
    permission_classes = [IsAdminUser]


class BlacklistRefreshToken(generics.CreateAPIView):
    authentication_classes = [JWTAuthentication]

    def post(self, request, *args, **kwargs):
        if request.data.get("refresh"):
            try:
                refresh_token = RefreshToken(request.data.get("refresh"))
                refresh_token.blacklist()
                return Response(
                    {"refresh": "Successfully blacklisted token aka logged-out!"},
                    status=status.HTTP_200_OK,
                )
            except TokenError:
                return Response(
                    {"refresh": "Token is already blacklisted"},
                    status=status.HTTP_401_UNAUTHORIZED,
                )
        return Response(
            {"refresh": "Token is missing"},
            status=status.HTTP_400_BAD_REQUEST,
        )
