from django.urls import path
from rest_framework.routers import DefaultRouter

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from .users.views import StaffRegistrationViewSet

from .views import FlightViewSet, OrderViewSet, UserViewSet, UserRegistrationViewSet

router = DefaultRouter()
router.register(r"flights", FlightViewSet, basename="flights")
router.register(r"orders", OrderViewSet, basename="orders")
router.register(r"users", UserViewSet, basename="users")
router.register(r"register", UserRegistrationViewSet, basename="register")
router.register(r"register/staff", StaffRegistrationViewSet, basename="register_staff")


urlpatterns = [
    path("auth/token/login/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("auth/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
]

urlpatterns.extend(router.urls)
