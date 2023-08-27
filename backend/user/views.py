from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import User
from .serializers import UserSerializers


# Perform CRUD in User
class UserManagement(APIView):
    def get(self, request):
        users_list = User.objects.all()
        serializers = UserSerializers(users_list, many=True)
        return Response(serializers.data)

    def post(self, request):
        serializers = UserSerializers(data=request.data)
        try:
            serializers.is_valid(raise_exception=True)
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        except ValidationError as e:
            error_message = e.detail
            return Response(error_message, status=status.HTTP_400_BAD_REQUEST)


class UserDetailManagement(APIView):
    def get(request, user_id):
        user = User.objects.filter(id=user_id)
        serializers = UserSerializers(user, many=True)
        return Response(serializers.data)

    def put(request, user_id):
        income_category = User.objects.get(id=user_id)
        serializers = UserSerializers(instance=income_category, data=request.data)
        try:
            serializers.is_valid(raise_exception=True)
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        except ValidationError as e:
            error_message = e.detail
            return Response(error_message, status=status.HTTP_400_BAD_REQUEST)

    def delete(request, user_id):
        item = get_object_or_404(User, id=user_id)
        item.delete()
        return Response(status=status.HTTP_202_ACCEPTED)
