from rest_framework import serializers
from usof_api.comments.models import Comment
from usof_api.serializers import NotNullSerializer
from usof_api.post.models import Post
from usof_api.post.serializers import AuthorSerializerField
# author_id = serializers.StringRelatedField()


class CommentSerializer(NotNullSerializer):
    class Meta:
        model = Comment
        fields = (
            'author', 'publish_date',
            'content', 'post_id'
        )


class UpdateCommentSerializer(NotNullSerializer):
    class Meta:
        model = Comment
        fields = ('content',)
