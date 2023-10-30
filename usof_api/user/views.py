from rest_framework import status, generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser, SAFE_METHODS
from django.shortcuts import redirect
from .models import User
from .serializers import UserSerializer
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
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get(self, request, username, *args, **kwargs):
        try:
            user = User.objects.get(login=username)
        except User.DoesNotExist:
            return Response("User does not exist!", status=status.HTTP_400_BAD_REQUEST)
        serialize = UserSerializer(user)
        return Response(serialize.data, status=status.HTTP_200_OK)

    def patch(self, request, username):
        current_user = User.objects.get(login=request.session['user'])
        try:
            user = User.objects.get(login=username)
        except User.DoesNotExist:
            return Response("User does not exist!", status=status.HTTP_400_BAD_REQUEST)

        if current_user.login == username or current_user.is_superuser:
            serializer = UserSerializer(instance=user, data=request.data, partial=True)
            serializer.is_valid(raise_exception=True)
            serializer.save()

            return Response(f"User's info has been updated: {user}", status=status.HTTP_200_OK)

        return Response("You arent authorize to update this user", status=status.HTTP_401_UNAUTHORIZED)

    def delete(self, request, username, *args, **kwargs):
        try:
            current_user = User.objects.get(login=request.session['user'])
            user = User.objects.get(login=username)
            if current_user.login == username or current_user.is_superuser:
                user.delete()

                if current_user.login == username:
                    del request.session['user']

                return Response("User has been deleted", status=status.HTTP_200_OK)
            else:
                return Response("You arent authorize to delete this user", status=status.HTTP_401_UNAUTHORIZED)
        except User.DoesNotExist:
            return Response("User does not exist!", status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response(f"Errors: {e}", status=status.HTTP_400_BAD_REQUEST)


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


# @api_view(['GET'])
# def get_current_user(request):
#     current_user = request.session['user']
#     return Response(current_user, status=status.HTTP_200_OK)
