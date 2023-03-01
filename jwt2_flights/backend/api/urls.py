from django.urls import path
from rest_framework.routers import DefaultRouter

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from .views import (
    FlightViewSet,
    OrderViewSet,
    UserViewSet,
)

router = DefaultRouter()
router.register(r"flights", FlightViewSet, basename="flights")
router.register(r"orders", OrderViewSet, basename="orders")
router.register(r"users", UserViewSet, basename="users")

urlpatterns = [
    path("auth/token/login/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("auth/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
]

urlpatterns.extend(router.urls)
