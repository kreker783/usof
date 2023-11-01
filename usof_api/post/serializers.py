from rest_framework import serializers
from usof_api.serializers import NotNullSerializer
from .models import Post
from usof_api.user.models import User


class AuthorSerializerField(serializers.Field):
    def to_representation(self, obj):
        try:
            user = User.objects.get(pk=obj)
            return user.login
        except:
            return "Error while getting author"

    def to_internal_value(self, data):
        return data


class PostSerializer(NotNullSerializer):
    author_id = AuthorSerializerField()
    post_id = serializers.IntegerField(source='pk', read_only=True)

    class Meta:
        model = Post
        fields = (
            'post_id', 'author_id', 'title',
            'status', 'content', 'categories'
        )


class PostCatSerializer(NotNullSerializer):
    post_id = serializers.IntegerField(source='pk', read_only=True)

    class Meta:
        model = Post
        fields = (
            'post_id', 'title', 'categories'
        )
