from models import Comment
from usof_api.serializers import NotNullSerializer


class CommentSerializer(NotNullSerializer):
    class Meta:
        model = Comment
        fields = (
            'author', 'publish_date', 'content'
        )
