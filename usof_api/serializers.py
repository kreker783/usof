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


class LoginSerializer(serializers.Serializer):

    login = serializers.CharField(
        label='login',
        write_only=True
    )
    email = serializers.CharField(
        label='email',
        write_only=True
    )
    password = serializers.CharField(
        label='password',
        style={'input_type': 'password'},
        trim_whitespace=False,
        write_only=True
    )

    def validate(self, attrs):
        login = attrs.get('login')
        email = attrs.get('email')
        password = attrs.get('password')

        if login and email and password:
            user = User.objects.filter(login=login)
            if user.exists():
                if user.first().email == email:
                    auth_user = authenticate(request=self.context.get('request'),
                                             login=login, password=password)
                else:
                    raise serializers.ValidationError({
                        "detail": "Wrong email for this user!",
                    })
            else:
                raise serializers.ValidationError({
                    "detail": "User does not exist in system",
                }, code='authorization')
        else:
            raise serializers.ValidationError({
                "detail": "Please provide 'login', 'password' and 'email' to log in",
            }, code='authorization')

        attrs['user'] = auth_user
        return attrs


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
