# auth/urls.py

from auth.views import UserLoginView, UserRegistrationView
from django.urls import path

urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='user_registration'),
    path('login/', UserLoginView.as_view(), name='user_login'),
]
