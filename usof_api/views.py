from django.shortcuts import render
from rest_framework import status, permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Post, Category, Comment, Like
from .serializers import PostSerializer, CategorySerializer, CommentSerializer, LikeSerializer


# Create your views here.
class PostApiView(APIView):
    def get(self, request, *args, **kwargs):
        posts = Post.objects.all()
        serialize = PostSerializer(posts, many=True)
        return Response(serialize.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        data = {
            "author": 'Test',
            "title": request.data.get("title"),
            "publish_date": request.data.get("publish", ""),
            "status": request.data.get("status", ""),
            "content": request.data.get("content", ""),
            "categories": request.data.get("categories", ""),
        }

        serialize = PostSerializer(data=data, required=False)
        if serialize.is_valid():
            serialize.save()
            return Response(serialize.data, status=status.HTTP_201_CREATED)
        return Response(serialize.errors, status=status.HTTP_400_BAD_REQUEST)
