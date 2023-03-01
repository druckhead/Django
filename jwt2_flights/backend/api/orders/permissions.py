from rest_framework.permissions import BasePermission


class OrderPermission(BasePermission):
    def has_permission(self, request, view):
        if view.action == "list":
            return request.user.is_authenticated and request.user.is_staff
        if view.action == "create":
            return request.user.is_authenticated
        elif view.action in ["update", "partial_update"]:
            # user with order id
            return request.user.is_authenticated and request.user.is_staff and (False)
