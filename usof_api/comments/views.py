from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from models import Comment
from serializers import CommentSerializer


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