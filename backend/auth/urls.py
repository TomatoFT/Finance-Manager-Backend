# auth/urls.py

from auth.views import (
    RefreshTokenView,
    UserLoginView,
    UserLogoutView,
    UserRegistrationView,
)
from django.urls import path

urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='user_registration'),
    path('login/', UserLoginView.as_view(), name='user_login'),
    path('logout/', UserLogoutView.as_view(), name='user_logout'),
    path('refresh/', RefreshTokenView.as_view(), name='refresh_token')
]
