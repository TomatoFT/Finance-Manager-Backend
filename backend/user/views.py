from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import User
from .serializers import UserSerializers


# Perform CRUD in User
@api_view(["GET"])
def get_all_users_informations(request):
    users_list = User.objects.all()
    serializers = UserSerializers(users_list, many=True)
    return Response(serializers.data)


@api_view(["GET"])
def get_user(request, user_id):
    user = User.objects.filter(user_id=user_id)
    serializers = UserSerializers(user, many=True)
    return Response(serializers.data)


@api_view(["POST"])
def add_user(request):
    serializers = UserSerializers(data=request.data)
    if serializers.is_valid():
        serializers.save()
    return Response(serializers.data)


@api_view(["PUT"])
def update_user(request, user_id):
    income_category = User.objects.get(user_id=user_id)
    data = UserSerializers(instance=income_category, data=request.data)
    print("DATA:", data)
    if data.is_valid():
        data.save()
        return Response(data.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(["DELETE", "GET"])
def delete_user(request, user_id):
    item = get_object_or_404(User, user_id=user_id)
    item.delete()
    return redirect(reverse("get_all_income_categories"))
