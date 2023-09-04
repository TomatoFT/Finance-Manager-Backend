import json

from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from user.models import User


class UserManagementTests(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_get_users(self):
        url = reverse("User Management")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_user(self):
        url = reverse("User Management")
        data = {
            "username": "testuser",
            "password": "testpassword",
            "email": "test@example.com",
            "phone": "1234567890",
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_user_invalid_data(self):
        url = reverse("User Management")
        data = {
            "username": "testuser",
            "password": "testpassword",
            "email": "invalid_email",
            "phone": "1234567890",
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class UserDetailManagementTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create(
            id=1,
            username="testuser",
            password="testpassword",
            email="test@example.com",
            phone="1234567890",
        )

    def test_get_user_detail(self):
        url = reverse("User Detail Management", args=[self.user.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_user_detail(self):
        url = reverse("User Detail Management", args=[self.user.id])
        data = {
            "username": "updateduser",
            "password": "updatedpassword",
            "email": "updated@example.com",
            "phone": "9876543210",
        }
        response = self.client.put(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_delete_user(self):
        url = reverse("User Detail Management", args=[self.user.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_202_ACCEPTED)
