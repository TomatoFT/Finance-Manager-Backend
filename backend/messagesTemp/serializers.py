from rest_framework import serializers

from .models import Notification


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = ["content", "created_at"]
