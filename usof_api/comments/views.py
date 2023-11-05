from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from datetime import date

import usof_api.permissions as permissions
from usof_api.comments.models import Comment
from usof_api.user.models import User
from usof_api.post.models import Post
from usof_api.comments.serializers import CommentSerializer


class CommentView(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get(self, request, post_id):
        comments = Comment.objects.filter(post_id=post_id)
        serialize = CommentSerializer(comments, many=True)
        # if serialize.is_valid():
        return Response(serialize.data, status=status.HTTP_200_OK)
        # return Response(serialize.errors, status=status.HTTP_200_OK)

    def post(self, request, post_id):
        request.data['author'] = request.session.get('user')
        request.data['post_id'] = post_id
        request.data['publish_date'] = date.today()

        serialize = CommentSerializer(data=request.data, many=True)

        if serialize.is_valid():
            serialize.save()
            return Response(serialize.validated_data, status=status.HTTP_200_OK)
        return Response(serialize.errors, status=status.HTTP_400_BAD_REQUEST)


class SpecificCommentView(APIView):

    def get(self, request, comment_id, *args, **kwargs):
        try:
            comment = Comment.objects.get(pk=comment_id)
            serialize = CommentSerializer(comment)
            return Response(serialize.data, status=status.HTTP_200_OK)
        except Comment.DoesNotExist:
            return Response("Comment with the specified id doesn't exist", status=status.HTTP_400_BAD_REQUEST)

    # def patch(self, request, category):
    #     try:
    #         spec_category = Category.objects.get(pk=category)
    #     except Category.DoesNotExist:
    #         return Response("Category does not exist!", status=status.HTTP_400_BAD_REQUEST)
    #
    #     serializer = CategorySerializer(instance=spec_category, data=request.data, partial=True)
    #     serializer.is_valid(raise_exception=True)
    #     serializer.save()
    #
    #     return Response("Categories info has been updated", status=status.HTTP_200_OK)
    #
    # def delete(self, request, category):
    #     try:
    #         spec_category = Category.objects.get(pk=category)
    #     except Category.DoesNotExist:
    #         return Response("Category does not exist!", status=status.HTTP_400_BAD_REQUEST)
    #
    #     spec_category.delete()
    #     return Response("Categories has been deleted", status=status.HTTP_200_OK)