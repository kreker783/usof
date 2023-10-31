from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Category
from usof_api.post.models import Post
from .serializers import CategorySerializer
import usof_api.permissions as permissions


# Create your views here.
class CategoryApiView(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get(self, request):
        categories = Category.objects.all()
        serialize = CategorySerializer(categories, many=True)
        return Response(serialize.data, status=status.HTTP_200_OK)

    def post(self, request):
        serialize = CategorySerializer(data=request.data, required=False)

        if serialize.is_valid():
            serialize.save()
            return Response(serialize.data, status=status.HTTP_201_CREATED)
        return Response(serialize.errors, status=status.HTTP_400_BAD_REQUEST)


class SpecificCategoryView(APIView):

    def get(self, request, category, *args, **kwargs):
        try:
            spec_category = Category.objects.get(pk=category)
            serialize = CategorySerializer(spec_category)
            return Response(serialize.data, status=status.HTTP_200_OK)
        except Category.DoesNotExist:
            return Response("Category with the specified id doesn't exist", status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, category):
        try:
            spec_category = Category.objects.get(pk=category)
        except Category.DoesNotExist:
            return Response("Category does not exist!", status=status.HTTP_400_BAD_REQUEST)

        serializer = CategorySerializer(instance=spec_category, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response("Categories info has been updated", status=status.HTTP_200_OK)


class PostsCategoriesView(APIView):
    def get(self, request, category, *args, **kwargs):
        try:
            spec_category = Category.objects.get(pk=category)
            posts = 
            serialize = PostSerializer(post)
            return Response(serialize.data.get('categories'), status=status.HTTP_200_OK)
        except Post.DoesNotExist:
            return Response("Post with the specified id doesn't exist", status=status.HTTP_400_BAD_REQUEST)