from rest_framework import serializers
from usof_api.serializers import NotNullSerializer
from .models import Post


class PostSerializer(NotNullSerializer):
    author = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = (
            'author', 'title',
            'status', 'content', 'categories'
        )

    def get_author(self, obj):
        return obj.author.login