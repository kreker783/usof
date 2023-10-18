import copy

from rest_framework import serializers
from django.contrib.auth import authenticate
from usof_api.user.models import User


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
