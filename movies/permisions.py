from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsAdminOrReadOnly(BasePermission):
    # Allow create, update, and delete requests for super users
    # read-only requests for any user

    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True

        if request.method in ['POST', 'PUT', 'DELETE']:
            return request.user.is_staff or request.user.is_superuser

        return True
