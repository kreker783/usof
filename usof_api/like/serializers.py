from usof_api.serializers import NotNullSerializer
from usof_api.like.models import Like
from rest_framework import serializers


class LikeSerializer(NotNullSerializer):

    class Meta:
        model = Like
        fields = (
            'publish_date', 'author', 'type',
            'post_id', 'comment_id'
        )
