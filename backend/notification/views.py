from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Notification
from .serializers import MessageSerializer


@api_view(["GET"])
def get_all_notifications_data(request):
    messages = Notification.objects.all()
    serializers = MessageSerializer(messages, many=True)
    return Response(serializers.data)


@api_view(["GET"])
def get_notification_data(request, notification_id):
    messages = Notification.objects.filter(notification_id=notification_id)
    serializers = MessageSerializer(messages)
    return Response(serializers.data)


@api_view(["POST"])
def add_notification_data(request):
    serializers = MessageSerializer(data=request.data)
    if serializers.is_valid():
        serializers.save()
    return Response(serializers.data)


# @api_view(["PUT"])
# def update_notification_data(request, notification_id):
#     messages = Notification.objects.get(notification_id=notification_id)
#     data = MessageSerializer(instance=messages, data=request.data)
#     print("DATA:", data)
#     if data.is_valid():
#         data.save()
#         return Response(data.data)
#     else:
#         return Response(status=status.HTTP_404_NOT_FOUND)


# @api_view(["DELETE", "GET"])
# def delete_notification_data(request, notification_id):
#     item = get_object_or_404(Notification, notification_id=notification_id)
#     item.delete()
#     return redirect(reverse("get_notification_data"))
