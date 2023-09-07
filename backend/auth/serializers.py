import logging

from django.contrib.auth.models import User as User_Auth
from rest_framework import serializers
from user.models import User

logger = logging.getLogger(__name__)

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'password', 'email', 'phone']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create(**validated_data)
        logger.warn(validated_data)
        User_Auth.objects.create_user(username=validated_data["username"], password=validated_data["password"])
        return user
