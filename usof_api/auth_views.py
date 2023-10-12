from rest_framework import status, permissions
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Post, Category, Comment, Like
from .serializers import PostSerializer, CategorySerializer, CommentSerializer, LikeSerializer


@api_view(['POST'])
def register(request):
    data = {
        'login': 'login',
        'password': 'password',
        'password_confirm': 'password_confirm',
        'email': 'email'
    }
