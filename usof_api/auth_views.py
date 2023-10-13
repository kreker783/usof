from rest_framework import status, permissions
from rest_framework.decorators import api_view
from django.shortcuts import redirect
from .managers import UserManager
from rest_framework.response import Response
from .models import Post, Category, Comment, Like, User
from .serializers import UserSerializer, CategorySerializer, CommentSerializer, LikeSerializer


@api_view(['POST'])
def register(request):
    data = {
        'login': request.data.get('login'),
        'password': request.data.get('password'),
        'password_confirm': request.data.get('password_confirm'),
        'email': request.data.get('email'),
        'role': request.data.get('role')
    }

    serializer = UserSerializer(data=data)
    if serializer.is_valid():
        if data['role'] == 'admin':
            permission = [permissions.IsAdminUser]
            user = UserManager
            user.create_admin(data['login'], data['password'], data)
        else:
            user = UserManager
            user.create_user(data['login'], data['password'], data)

        return redirect('/usof/api/users/')

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
