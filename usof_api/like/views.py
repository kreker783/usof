from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

from usof_api import permissions
from usof_api.like.models import Like
from usof_api.like.serializers import LikeSerializer
from usof_api.comments.models import Comment
from usof_api.post.models import Post


# Create your views here.
class CommentLikeView(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get(self, request, id):
        if validate_if_comment_exist(id):
            like = Like.objects.filter(comment_id=id)
            serialize = LikeSerializer(like, many=True)
            return Response(serialize.data, status=status.HTTP_200_OK)

        return Response("Comment with provided ID does not exist", status=status.HTTP_400_BAD_REQUEST)

    def post(self, request, id):
        if validate_if_comment_exist(id):
            request.data['author'] = request.session.get('user')
            request.data['comment_id'] = id

            serialize = LikeSerializer(data=request.data)

            if serialize.is_valid():
                serialize.save()
                return Response(serialize.validated_data, status=status.HTTP_200_OK)
            return Response(serialize.errors, status=status.HTTP_400_BAD_REQUEST)

        return Response("Comment with provided ID does not exist", status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        author = request.session.get('user')
        try:
            like = Like.objects.get(comment_id=id, author=author)
        except Like.DoesNotExist:
            return Response("Comment does not exist!", status=status.HTTP_400_BAD_REQUEST)

        like.delete()

        return Response("Like has been deleted", status=status.HTTP_200_OK)


class PostLikeView(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get(self, request, id):
        if validate_if_post_exist(id):
            like = Like.objects.filter(post_id=id)
            serialize = LikeSerializer(like, many=True)
            return Response(serialize.data, status=status.HTTP_200_OK)

        return Response("Post with provided ID does not exist", status=status.HTTP_400_BAD_REQUEST)

    def post(self, request, id):
        if validate_if_post_exist(id):
            request.data['author'] = request.session.get('user')
            request.data['post_id'] = id

            serialize = LikeSerializer(data=request.data)

            if serialize.is_valid():
                serialize.save()
                return Response(serialize.validated_data, status=status.HTTP_200_OK)
            return Response(serialize.errors, status=status.HTTP_400_BAD_REQUEST)

        return Response("Post with provided ID does not exist", status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        author = request.session.get('user')
        try:
            like = Like.objects.get(post_id=id, author=author)
        except Like.DoesNotExist:
            return Response("Post does not exist!", status=status.HTTP_400_BAD_REQUEST)

        like.delete()

        return Response("Like has been deleted", status=status.HTTP_200_OK)


def validate_if_post_exist(post_id):
    try:
        post = Post.objects.get(pk=post_id)
    except Post.DoesNotExist:
        return False

    return True


def validate_if_comment_exist(post_id):
    try:
        post = Comment.objects.get(pk=post_id)
    except Comment.DoesNotExist:
        return False

    return True
