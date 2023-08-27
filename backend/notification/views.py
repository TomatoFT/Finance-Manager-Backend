# from django.shortcuts import get_object_or_404, redirect
# from django.urls import reverse
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Notification
from .serializers import NoticationSerializer


class NotificationManagement(APIView):
    def get(request):
        messages = Notification.objects.all()
        serializers = NoticationSerializer(messages, many=True)
        return Response(serializers.data)

    def post(self, request):
        serializers = NoticationSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
        return Response(serializers.data)


class NotificationDetailManagement(APIView):
    def get(self, request, notification_id):
        messages = Notification.objects.filter(notification_id=notification_id)
        serializers = NoticationSerializer(messages)
        return Response(serializers.data)
