from rest_framework import status, permissions
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Post, Category, Comment, Like
from .serializers import PostSerializer, CategorySerializer, CommentSerializer, LikeSerializer


@api_view(['POST'])
def create_user(request):
    data = {
        'login': 'login',
        'password'
    }
