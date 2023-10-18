from rest_framework import serializers

from usof_api.serializers import NotNullSerializer
from .models import User


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
