from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import mixins, status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, BasePermission
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet, GenericViewSet

from imdb_app.models import Review
from imdb_app.serializers.reviews import ReviewSerializer


# only logged-in users can create a review
# only user that created a review can update/delete it
class ReviewsPermissions(BasePermission):
    def has_permission(self, request, view):
        if request.method in ['POST']:
            return request.user.is_authenticated
        return True

    def has_object_permission(self, request, view, obj):
        if request.method in ['PATCH', 'PUT', 'DELETE']:
            return request.user.is_authenticated and request.user.id == obj.user_id
        return True


class ReviewsViewSet(ModelViewSet):

    queryset = Review.objects.all()

    permission_classes = [ReviewsPermissions]

    # we need different serializers for different actions
    serializer_class = ReviewSerializer

    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['movie',]

    def get_queryset(self):
        qs = self.queryset
        if self.action == 'list':
            if 'user' in self.request.query_params and self.request.query_params['user'] == 'me':
                qs = qs.filter(user=self.request.user)
        return qs

    def create(self, request, *args, **kwargs):
        request_data = request.data
        if "user" not in request_data:
            request_data["user"] = request.user.id

        if Review.objects.filter(user_id=request_data["user"], movie_id=request_data["movie"]):
            return Response(data={"reviews": "user already posted review"}, status=status.HTTP_400_BAD_REQUEST)

        serializer = self.get_serializer(data=request_data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
