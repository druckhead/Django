from rest_framework import viewsets
from rest_framework_simplejwt.authentication import JWTAuthentication

from .models import Order
from .permissions import OrderPermission
from .serializers import OrderSerializer


class OrderViewSet(viewsets.ModelViewSet):
    serializer_class = OrderSerializer
    queryset = Order.objects.all()
    permission_classes = [OrderPermission]
    authentication_classes = [JWTAuthentication]
