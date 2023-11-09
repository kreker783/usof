from rest_framework import serializers

from usof_api.serializers import NotNullSerializer
from .models import User


class UserSerializer(NotNullSerializer):
    class Meta:
        model = User
        fields = (
            'login', 'email', 'full_name',
            'picture', 'rating', 'is_staff',
            'is_active', 'is_superuser'
        )

        def update(self, instance, validated_data):
            """
            Update and return an existing `User` instance, given the validated data.
            """
            instance.login = validated_data.get('login', instance.login)
            instance.email = validated_data.get('email', instance.email)
            instance.full_name = validated_data.get('full_name', instance.full_name)
            instance.picture = validated_data.get('picture', instance.picture)
            instance.rating = validated_data.get('rating', instance.rating)
            instance.save()
            return instance

        def validate(self, attrs):
            if attrs['password'] != attrs['password_confirm']:
                raise serializers.ValidationError({
                    "password": "Password fields didn't match"
                })
            return attrs

        def create(self):
            return User(**self.validated_data)
