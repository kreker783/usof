from rest_framework import status, permissions
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import redirect
from .models import Post, Category, Comment, Like, User
from .serializers import UserSerializer, PostSerializer, CategorySerializer, CommentSerializer, LikeSerializer



class UserView()


@api_view(['GET'])
def get_users(request):
    users = User.objects.all()
    serialize = UserSerializer(users, many=True)
    return Response(serialize.data, status=status.HTTP_200_OK)


@api_view(['GET'])
def get_user(request, username):
    user = User.objects.get(login=username)
    data = {
        "login": user.login,
        "staff": user.is_superuser
    }
    return Response(data, status=status.HTTP_200_OK)


@api_view(['POST'])
def create_admin(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        # permission = [permissions.IsAdminUser]
        user = User.objects.create_superuser(request.data.get('login'),
                                             request.data.get('password'),
                                             **serializer.validated_data)

        return redirect('/usof/api/users/')

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
