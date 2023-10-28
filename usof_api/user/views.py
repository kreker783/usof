from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser, SAFE_METHODS
from rest_framework.decorators import api_view
from django.shortcuts import redirect
from .models import User
from .serializers import UserSerializer
from .form import PictureForm
from rest_framework import permissions


class IsAdminOrReadOnly(IsAdminUser):

    def has_permission(self, request, view):
        is_admin = super().has_permission(request, view)
        return request.method in SAFE_METHODS or is_admin


class IsAuthorPermission(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        try:
            user = User.objects.get(request.session['user'])
        except:
            return False

        if user.is_superuser or request.method in SAFE_METHODS:
            return True

        if user == obj.author:
            return True

        return False


class UsersView(APIView):
    permission_classes = [IsAdminOrReadOnly]

    def get(self, request, username=None):
        if username:
            return self.get_user(request, username)
        user = User.objects.all()
        serialize = UserSerializer(user, many=True)
        return Response(serialize.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = User.objects.create_superuser(request.data.get('login'),
                                                 request.data.get('password'),
                                                 **serializer.validated_data)

            return redirect('/usof/api/users/')

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SpecificUserView(APIView):
    def get(self, request, username):
        try:
            user = User.objects.get(login=username)
            print(user.is_active)
        except User.DoesNotExist:
            user = None
        serialize = UserSerializer(user)
        return Response(serialize.data, status=status.HTTP_200_OK)

# @api_view(['PATCH'])
# @csrf_exempt
# def update_users_avatar(request):
#     try:
#         user = request.session['user']
#     except:
#         return Response("You have to log in first!", status=status.HTTP_401_UNAUTHORIZED)
#
#     form = PictureForm(user, request.FILES)
#
#     if form.is_valid():
#         form.save()
#         return Response("Image has been updated", status=status.HTTP_200_OK)
#
#     return Response(form.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def get_current_user(request):
    current_user = request.user
    return Response(request.id, status=status.HTTP_200_OK)
