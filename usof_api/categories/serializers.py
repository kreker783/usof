from usof_api.serializers import NotNullSerializer
from usof_api.categories.models import Category


class CategorySerializer(NotNullSerializer):
    class Meta:
        model = Category
        fields = (
            'title', 'description'
        )
