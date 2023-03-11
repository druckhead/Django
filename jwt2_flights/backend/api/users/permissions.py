from rest_framework.permissions import BasePermission


class UserPermission(BasePermission):
    def has_permission(self, request, view):
        if view.action in ["retrieve"]:
            return request.user.is_authenticated
        if view.action in ["list"]:
            return request.user.is_authenticated and request.user.is_staff
        return True

    def has_object_permission(self, request, view, obj):
        if view.action in ["retrieve"]:
            return request.user.is_authenticated and request.user.id == obj.id
