import logging

from django.contrib.auth.models import User as User_Auth
from rest_framework import serializers
from user.models import User

logger = logging.getLogger(__name__)

class UserSerializer(serializers.ModelSerializer):
    """
    Serializer for the User model.

    This serializer handles the serialization and deserialization of User objects.

    """

    class Meta:
        model = User
        fields = ['id', 'username', 'password', 'email', 'phone']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        """
        Create a new user.

        This method creates a new User object based on the provided validated data.

        Args:
            validated_data (dict): Validated data for creating a new user.

        Returns:
            User: The created User object.

        """

        user = User.objects.create(**validated_data)
        logger.warn(validated_data)
        User_Auth.objects.create_user(username=validated_data["username"],
                                      password=validated_data["password"])
        return user
