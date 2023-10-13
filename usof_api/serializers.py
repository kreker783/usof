from rest_framework import serializers
from .models import User, Post, Category, Comment, Like


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['login', 'email', 'full_name', 'picture', 'rating']


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = (
            'author', 'title',
            'status', 'content', 'categories')


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'


class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = '__all__'
