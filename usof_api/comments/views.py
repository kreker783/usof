from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from datetime import date

import usof_api.permissions as permissions
from usof_api.comments.models import Comment
from usof_api.post.models import Post
from usof_api.user.models import User
from usof_api.comments.serializers import CommentSerializer, UpdateCommentSerializer


class CommentView(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get(self, request, post_id):
        if validate_if_post_exist(post_id):

            comments = Comment.objects.filter(post_id=post_id)
            serialize = CommentSerializer(comments, many=True)
            # if serialize.is_valid():
            return Response(serialize.data, status=status.HTTP_200_OK)
            # return Response(serialize.errors, status=status.HTTP_200_OK)

        return Response("Post with provided ID does not exist", status=status.HTTP_400_BAD_REQUEST)

    def post(self, request, post_id):
        if validate_if_post_exist(post_id):

            request.data['author'] = request.session.get('user')
            request.data['post_id'] = post_id
            request.data['publish_date'] = date.today()

            serialize = CommentSerializer(data=request.data)

            if serialize.is_valid():
                serialize.save()
                return Response(serialize.validated_data, status=status.HTTP_200_OK)
            return Response(serialize.errors, status=status.HTTP_400_BAD_REQUEST)

        return Response("Post with provided ID does not exist", status=status.HTTP_400_BAD_REQUEST)


class SpecificCommentView(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get(self, request, comment_id, *args, **kwargs):
        try:
            comment = Comment.objects.get(pk=comment_id)
            serialize = CommentSerializer(comment)
            return Response(serialize.data, status=status.HTTP_200_OK)
        except Comment.DoesNotExist:
            return Response("Comment with the specified id doesn't exist", status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, comment_id):
        try:
            comment = Comment.objects.get(pk=comment_id)
        except Comment.DoesNotExist:
            return Response("Comment with the specified id doesn't exist", status=status.HTTP_400_BAD_REQUEST)

        user = request.session.get('user')

        if user == comment.author:
            comment.content = request.data.get('content')
            comment.save()

            return Response("Comment has been updated", status=status.HTTP_200_OK)
        else:
            return Response("You arent comment author, so you can't change it", status=status.HTTP_401_UNAUTHORIZED)

    def delete(self, request, comment_id):
        try:
            comment = Comment.objects.get(pk=comment_id)
        except Comment.DoesNotExist:
            return Response("Category does not exist!", status=status.HTTP_400_BAD_REQUEST)

        user = request.session.get('user')

        if user == comment.author:
            comment.delete()

            return Response("Comment has been deleted", status=status.HTTP_200_OK)
        else:
            return Response("You arent comment author, so you can't delete it", status=status.HTTP_401_UNAUTHORIZED)


def validate_if_post_exist(post_id):
    try:
        post = Post.objects.get(pk=post_id)
    except Post.DoesNotExist:
        return False

    return True
