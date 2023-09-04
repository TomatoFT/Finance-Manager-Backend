from notification.models import Notification
from notification.serializers import NoticationSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView


class NotificationManagement(APIView):
    def get(request):
        messages = Notification.objects.all()
        serializer = NoticationSerializer(messages, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = NoticationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class NotificationDetailManagement(APIView):
    def get(self, request, notification_id):
        messages = Notification.objects.filter(notification_id=notification_id)
        serializer = NoticationSerializer(messages)
        return Response(serializer.data, status=status.HTTP_200_OK)
