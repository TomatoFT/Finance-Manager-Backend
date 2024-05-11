import logging

from auth.serializers import UserSerializer
from django.contrib.auth import authenticate, logout
from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken

logger = logging.getLogger(__name__)

class UserRegistrationView(generics.CreateAPIView):
    """
    API view for user registration.

    This view allows creating a new user account.

    """

    serializer_class = UserSerializer


class UserLoginView(APIView):
    """
    API view for user login.

    This view allows authenticating a user and generating access and refresh tokens.

    """

    def post(self, request):
        """
        Authenticate a user and generate tokens.

        This method authenticates a user based on the provided username and password, and
        generates access and refresh tokens if the authentication is successful.

        Args:
            request (Request): The HTTP request object.

        Returns:
            Response: Serialized data of the generated tokens. Return invalid credentials if
                        the authentication failed.

        """

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
            return Response({'error': 'Invalid credentials'},
                            status=status.HTTP_400_BAD_REQUEST)


class UserLogoutView(APIView):
    """
    API view for user logout.

    This view allows logging out a user and invalidating the refresh token.

    """

    permission_classes = [IsAuthenticated]

    def post(self, request):
        """
        Logout a user and invalidate the refresh token.

        This method logs out a user by invalidating the refresh token associated with the user.

        Args:
            request (Request): The HTTP request object.

        Returns:
            Response: Response indicating the success or failure of the logout operation.

        """

        refresh_token = request.data.get('refresh_token')
        logger.warn(refresh_token)
        try:
            token = RefreshToken(refresh_token)
            logger.warn(token)
            token.blacklist()
            return Response({'message': 'Logout successful'})
        except Exception as e:
            return Response({'error': 'Invalid token'},
                            status=status.HTTP_400_BAD_REQUEST)


class RefreshTokenView(APIView):
    """
    API view for refreshing an access token.

    This view allows refreshing an access token using a valid refresh token.

    """

    def post(self, request):
        """
        Refresh an access token.

        This method refreshes an access token using a valid refresh token.

        Args:
            request (Request): The HTTP request object.

        Returns:
            Response: Serialized data of the new access token.

        """

        refresh_token = request.data.get('refresh_token')

        try:
            token = RefreshToken(refresh_token)
            access_token = str(token.access_token)
            return Response({'access_token': access_token})
        except Exception as e:
            return Response({'error': 'Invalid token'},
                            status=status.HTTP_400_BAD_REQUEST)
