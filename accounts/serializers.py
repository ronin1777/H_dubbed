import logging

from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.exceptions import AuthenticationFailed

from accounts.models import User


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(min_length=8
                                     , max_length=68, write_only=True)

    class Meta:
        model = User
        fields = ['email', 'username', 'password']

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user


class EmailVerificationSerializer(serializers.ModelSerializer):
    token = serializers.CharField(max_length=555)

    class Meta:
        model = User
        fields = ['token']


class LogInSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        if user.verified_email is False:
            raise AuthenticationFailed('you must active your email')
        else:
            token = super().get_token(user)
            user_data = UserSerializer(user).data
            for key, value in user_data.items():
                if key != "id":
                    token[key] = value
            return token


class LogoutSerializer(serializers.Serializer):
    refresh = serializers.CharField()
    default_error_messages = {"bad_token": "Token is invalid or expired"}

    def validate(self, data):
        self.token = data["refresh"]
        return data

    def save(self, **kwargs):
        try:
            RefreshToken(self.token).blacklist()
        except Exception as e:
            logging.error(f"Failed to blacklist token: {e}")
