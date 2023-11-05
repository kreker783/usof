from usof_api.serializers import NotNullSerializer
from usof_api.like.models import Like
from rest_framework import serializers


class LikeSerializer(NotNullSerializer):
    type_display = serializers.SerializerMethodField()

    class Meta:
        model = Like
        fields = (
            'author', 'publish_date',
            'post_id', 'comment_id', 'type_display'
        )

        def get_type_display(self, obj):
            return "Like" if obj.type else "Dislike"