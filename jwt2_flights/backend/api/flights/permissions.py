from rest_framework.permissions import BasePermission


class FlightPermission(BasePermission):
    def has_permission(self, request, view):
        """
        PERMISSIONS
            list
            retrieve
            create
            update
            update_partial
            destroy
        """
        if view.action in ["list", "retrieve"]:
            return True
        elif view.action in ["create", "update", "partial_update", "destroy"]:
            return request.user.is_authenticated and request.user.is_staff
        return False

    # def has_object_permission(self, request, view, obj):
    #     # Deny actions on objects if the user is not authenticated
    #     if not request.user.is_authenticated():
    #         return False

    # if view.action == 'list':
    #     return obj == request.user or request.user.is_admin
    # elif view.action == 'retrieve':
    #     return obj == request.user
    # else:
    #     return False
