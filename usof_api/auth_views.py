from rest_framework import status, permissions
from rest_framework.decorators import api_view
from django.shortcuts import redirect
from django.core import management
from .managers import UserManager
from rest_framework.response import Response
from .models import Post, Category, Comment, Like, User
from .serializers import UserSerializer, CategorySerializer, CommentSerializer, LikeSerializer


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

        return redirect('/usof/api/users/')

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
