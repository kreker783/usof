from rest_framework import status, permissions
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Post, Category, Comment, Like, User
from .serializers import UserSerializer, PostSerializer, CategorySerializer, CommentSerializer, LikeSerializer


@api_view(['GET'])
def get_users(request):
    users = User.objects.all()
    serialize = UserSerializer(users, many=True)
    return Response(serialize.data, status=status.HTTP_200_OK)
