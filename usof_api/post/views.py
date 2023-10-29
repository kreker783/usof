from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Post
from usof_api.user.models import User
from .serializers import PostSerializer
import usof_api.permissions as permissions


# Create your views here.
class PostApiView(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get(self, request):
        posts = Post.objects.all()
        serialize = PostSerializer(posts, many=True)
        return Response(serialize.data, status=status.HTTP_200_OK)

    def post(self, request):
        request.data['author'] = User.objects.get(login=request.session.get('user')).pk

        serialize = PostSerializer(data=request.data, required=False)
        if serialize.is_valid():
            serialize.save()
            return Response(serialize.data, status=status.HTTP_201_CREATED)
        return Response(serialize.errors, status=status.HTTP_400_BAD_REQUEST)
