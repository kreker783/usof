from rest_framework import status, permissions
from rest_framework.views import APIView
from rest_framework.decorators import permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser, SAFE_METHODS
from django.shortcuts import redirect
from .models import User
from .serializers import UserSerializer


class IsAdminOrReadOnly(IsAdminUser):

    def has_permission(self, request, view):
        is_admin = super().has_permission(request, view)
        return request.method in SAFE_METHODS or is_admin


class UsersView(APIView):
    permission_classes = [IsAdminOrReadOnly]

    # @permission_classes([IsAdminUser])
    def get_user(self, request, username):
        user = User.objects.get(login=username)
        data = {
            "login": user.login,
            "staff": user.is_staff,
            "admin": user.is_superuser
        }
        return Response(data, status=status.HTTP_200_OK)

    def get(self, request, username=None):
        if username:
            return self.get_user(request, username)
        user = User.objects.all()
        serialize = UserSerializer(user, many=True)
        return Response(serialize.data, status=status.HTTP_200_OK)

    # @permission_classes([IsAuthenticated, IsAdminUser])
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            permission = [permissions.IsAdminUser]
            user = User.objects.create_superuser(request.data.get('login'),
                                                 request.data.get('password'),
                                                 **serializer.validated_data)

            return redirect('/usof/api/users/')

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
