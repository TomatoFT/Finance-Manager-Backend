from notification.models import Notification
from rest_framework import serializers


class NoticationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = "__all__"
