import copy

from rest_framework import serializers
from django.contrib.auth import authenticate
from .models import User, Post, Category, Comment, Like


class NotNullSerializer(serializers.ModelSerializer):

    def to_representation(self, instance):
        ret = super().to_representation(instance)
        not_null_ret = copy.deepcopy(ret)
        for key in ret.keys():
            if not ret[key]:
                not_null_ret.pop(key)
        return not_null_ret


class UserSerializer(NotNullSerializer):
    class Meta:
        model = User
        fields = (
            'login', 'email', 'full_name',
            'picture', 'rating', 'is_staff'
        )

        def validate(self, attrs):
            if attrs['password'] != attrs['password_confirm']:
                raise serializers.ValidationError({
                    "password": "Password fields didn't match"
                })
            return attrs


class LoginSerializer(NotNullSerializer):

    class Meta:
        model = User
        fields = (
            'login', 'email',
            'password'
        )
        extra_kwargs = {
            'login': {'required': True},
            'email': {'required': True},
            'password': {'required': True}
        }


class PostSerializer(NotNullSerializer):
    class Meta:
        model = Post
        fields = (
            'author', 'title',
            'status', 'content', 'categories'
        )


class CategorySerializer(NotNullSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class CommentSerializer(NotNullSerializer):
    class Meta:
        model = Comment
        fields = '__all__'


class LikeSerializer(NotNullSerializer):
    class Meta:
        model = Like
        fields = '__all__'
