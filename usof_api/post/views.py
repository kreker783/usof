
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
        request.data['author_id'] = User.objects.get(login=request.session.get('user')).pk
        serialize = PostSerializer(data=request.data, required=False)

        if serialize.is_valid():
            serialize.save()
            return Response(serialize.data, status=status.HTTP_201_CREATED)
        return Response(serialize.errors, status=status.HTTP_400_BAD_REQUEST)


class SpecificPostView(APIView):
    def get(self, request, post_id, *args, **kwargs):
        try:
            post = Post.objects.get(pk=post_id)
            serialize = PostSerializer(post)
            return Response(serialize.data, status=status.HTTP_200_OK)
        except Post.DoesNotExist:
            return Response("Post with the specified id doesn't exist", status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, post_id):
        current_user = User.objects.get(login=request.session.get('user'))
        try:
            post = Post.objects.get(pk=post_id)
        except Post.DoesNotExist:
            return Response("Post does not exist!", status=status.HTTP_400_BAD_REQUEST)

        if current_user.login == post.author.login or current_user.is_superuser:
            serializer = PostSerializer(instance=post, data=request.data, partial=True)
            serializer.is_valid(raise_exception=True)
            serializer.save()

            return Response("Post's info has been updated", status=status.HTTP_200_OK)

        return Response(f"You arent authorize to update this post", status=status.HTTP_401_UNAUTHORIZED)


class CategoriesPostView(APIView):
    def get(self, request, post_id, *args, **kwargs):
        try:
            post = Post.objects.get(pk=post_id)
            serialize = PostSerializer(post)
            return Response(serialize.data.get('categories'), status=status.HTTP_200_OK)
        except Post.DoesNotExist:
            return Response("Post with the specified id doesn't exist", status=status.HTTP_400_BAD_REQUEST)