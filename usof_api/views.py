from django.shortcuts import render
from rest_framework import status, permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Post, Category, Comment, Like
from .serializers import PostSerializer, CategorySerializer, CommentSerializer, LikeSerializer


# Create your views here.
class PostApiView(APIView):
    def get(self, request, *args, **kwargs):
        posts = Post
        serialize = PostSerializer(posts, many=True)
        return Response(serialize.data, status=status.HTTP_200_OK)
