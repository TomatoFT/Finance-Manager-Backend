from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from rest_framework.views import APIView
from user.models import User
from user.serializers import UserSerializers


# Perform CRUD in User
class UserManagement(APIView):
    def get(self, request):
        users_list = User.objects.all()
        serializer = UserSerializers(users_list, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = UserSerializers(data=request.data)
        try:
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except ValidationError as e:
            error_message = e.detail
            return Response(error_message, status=status.HTTP_400_BAD_REQUEST)


class UserDetailManagement(APIView):
    def get(self, request, user_id):
        user = User.objects.get(id=user_id)
        serializer = UserSerializers(user)
        return Response(serializer.data)

    def put(self, request, user_id):
        user = User.objects.get(id=user_id)
        serializer = UserSerializers(instance=user, data=request.data)
        try:
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except ValidationError as e:
            error_message = e.detail
            return Response(error_message, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, user_id):
        matched_user = get_object_or_404(User, id=user_id)
        matched_user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
