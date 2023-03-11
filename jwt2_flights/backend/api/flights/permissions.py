from rest_framework.permissions import BasePermission


class FlightPermission(BasePermission):
    def has_permission(self, request, view):
        if view.action in ["create", "update", "partial_update"]:
            return request.user.is_authenticated and request.user.is_staff
        return True

    def has_object_permission(self, request, view, obj):
        return True