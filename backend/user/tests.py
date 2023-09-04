import json

from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from user.models import User


class UserManagementTests(TestCase):
    CREATE_INVALID_USER_TEST = "user/test/create_invalid_user.json"
    CREATE_USER_TEST = "user/test/create_user.json"
    UPDATE_USER_TEST = "user/test/update_user.json"
    UPDATE_INVALID_USER_TEST = "user/test/update_invalid_user.json"

    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create(
            username="testuser",
            password="testpassword",
            email="test@example.com",
            phone="1234567890",
        )

    def test_get_users(self):
        url = reverse("User Management")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_user(self):
        url = reverse("User Management")
        data = self.get_the_data_from_json_file(json_file_path=self.CREATE_USER_TEST)
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_user_invalid_data(self):
        url = reverse("User Management")
        data = self.get_the_data_from_json_file(
            json_file_path=self.CREATE_INVALID_USER_TEST
        )
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_get_user_detail(self):
        url = reverse("User Detail Management", args=[self.user.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_user_detail(self):
        url = reverse("User Detail Management", args=[self.user.id])
        data = self.get_the_data_from_json_file(json_file_path=self.UPDATE_USER_TEST)
        response = self.client.put(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_update_user_detail(self):
        url = reverse("User Detail Management", args=[self.user.id])
        data = self.get_the_data_from_json_file(
            json_file_path=self.UPDATE_INVALID_USER_TEST
        )
        response = self.client.put(url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_delete_user(self):
        url = reverse("User Detail Management", args=[self.user.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def get_the_data_from_json_file(self, json_file_path):
        with open(json_file_path, "r") as json_file:
            data = json.load(json_file)
        return data
