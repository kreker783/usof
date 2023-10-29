from rest_framework import permissions


class IsAuthenticatedOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        # Check if the 'user' session variable exists and is not None
        return request.session.get('user') is not None
