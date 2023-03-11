from rest_framework.permissions import BasePermission


class OrderPermission(BasePermission):
    def has_permission(self, request, view):
        if view.action == "create":
            return request.user.is_authenticated
        if view.action in ["update", "partial_update", "retrieve"]:
            return True
        if view.action == "list":
            return request.user.is_authenticated and request.user.is_staff

    def has_object_permission(self, request, view, obj):
        if view.action in ["update", "partial_update", "retrieve"]:
            if request.user.is_staff:
                return request.user.is_authenticated and request.user.is_staff
            else:
                return request.user.is_authenticated and request.user.id == obj.user_id
