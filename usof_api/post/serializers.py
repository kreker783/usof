from usof_api.serializers import NotNullSerializer
from .models import Post


class PostSerializer(NotNullSerializer):
    class Meta:
        model = Post
        fields = (
            'author', 'title',
            'status', 'content', 'categories'
        )
