from auth.serializers import UserSerializer
from django.contrib.auth import authenticate
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken


class UserRegistrationView(generics.CreateAPIView):
    serializer_class = UserSerializer


class UserLoginView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        user = authenticate(username=username, password=password)
        if user is not None:
            refresh = RefreshToken.for_user(user)
            return Response({
                'access_token': str(refresh.access_token),
                'refresh_token': str(refresh),
            })
        else:
            return Response({'error': 'Invalid credentials'}, status=400)
