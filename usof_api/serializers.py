import copy

from rest_framework import serializers
from django.contrib.auth import authenticate
from .models import Category, Comment, Like


class NotNullSerializer(serializers.ModelSerializer):

    def to_representation(self, instance):
        ret = super().to_representation(instance)
        not_null_ret = copy.deepcopy(ret)
        for key in ret.keys():
            if not ret[key]:
                not_null_ret.pop(key)
        return not_null_ret


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
