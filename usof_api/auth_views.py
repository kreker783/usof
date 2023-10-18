from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework import views
from django.contrib.auth import login, authenticate, logout
from django.shortcuts import redirect
from rest_framework.response import Response
from .models import Post, Category, Comment, Like, User
from .serializers import UserSerializer, LoginSerializer


@api_view(['POST'])
def register(request):

    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        if request.data.get('is_staff'):
            # permission = [permissions.IsAdminUser]
            user = User.objects.create_superuser(request.data.get('login'),
                                                 request.data.get('password'),
                                                 **serializer.validated_data)
        else:
            serializer.save()

        return redirect('users')

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def loginView(request):
    serialize = LoginSerializer(data=request.data)
    serialize.is_valid(raise_exception=True)
    user = serialize.validated_data['user']
    login(request, user)
    return redirect('users')


@api_view(['GET', 'POST'])
def logoutView(request):
    logout(request)
    return redirect('users')