from rest_framework import serializers
from usof_api.serializers import NotNullSerializer
from usof_api.categories.models import Category


class CategorySerializer(NotNullSerializer):
    # category_id = serializers.IntegerField(source='pk', read_only=True)

    class Meta:
        model = Category
        fields = (
            'title', 'description'
        )
