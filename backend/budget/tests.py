import json
import logging
from datetime import datetime, timezone

from budget.models import Budget, IncomeCategory
from budget.serializers import BudgetSerializer
from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from user.models import User

logger = logging.getLogger(__name__)


class BudgetManagementTests(TestCase):
    CREATE_TEST_PATH = "budget/test/create_budget_test.json"
    CREATE_INVALID_TEST_PATH = "budget/test/create_invalid_budget_test.json"
    UPDATE_TEST_PATH = "budget/test/update_budget_test.json"
    UPDATE_INVALID_TEST_PATH = "budget/test/update_invalid_budget_test.json"

    def setUp(self):
        self.client = APIClient()

    def test_get_budgets(self):
        url = reverse("Budget Management")
        response = self.client.get(url)
        expenses = Budget.objects.all()
        serializer = BudgetSerializer(expenses, many=True)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

    def test_create_budget(self):
        url = reverse("Budget Management")
        _ = self.create_data()
        data = self.get_the_data_from_json_file(json_file_path=self.CREATE_TEST_PATH)
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        budget = Budget.objects.last()
        self.assertEqual(budget.name, data["name"])
        self.assertEqual(budget.income_category.id, data["income_category"])
        self.assertEqual(budget.user.id, data["user"])
        self.assertEqual(budget.always_notify, data["always_notify"])
        self.assertEqual(budget.amount, data["amount"])

    def test_create_budget_with_invalid_data(self):
        url = reverse("Budget Management")
        _ = self.create_data()
        data = self.get_the_data_from_json_file(
            json_file_path=self.CREATE_INVALID_TEST_PATH
        )
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(Budget.objects.count(), 0)

    def test_update_budget_with_invalid_data(self):
        url = reverse("Budget Management")
        budget = self.create_data(created_budget=True)
        url = reverse("Budget Detail Management", args=[budget.id])
        data = self.get_the_data_from_json_file(
            json_file_path=self.UPDATE_INVALID_TEST_PATH
        )
        response = self.client.put(url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_update_budget(self):
        url = reverse("Budget Management")
        budget = self.create_data(created_budget=True)
        url = reverse("Budget Detail Management", args=[budget.id])
        data = self.get_the_data_from_json_file(json_file_path=self.UPDATE_TEST_PATH)
        response = self.client.put(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        budget.refresh_from_db()
        self.assertEqual(budget.name, data["name"])
        self.assertEqual(budget.income_category.id, data["income_category"])
        self.assertEqual(budget.user.id, data["user"])
        self.assertEqual(budget.always_notify, data["always_notify"])
        self.assertEqual(budget.date, datetime.fromisoformat(data["date"]))
        self.assertEqual(budget.amount, data["amount"])

    def test_delete_budget(self):
        url = reverse("Budget Management")
        budget = self.create_data(created_budget=True)
        url = reverse("Budget Detail Management", args=[budget.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Budget.objects.count(), 0)

    def create_data(self, created_budget=False):
        user = User.objects.create(
            id=1, username="abc", password="abc", email="abc@a.com", phone=121112222111
        )
        income_category = IncomeCategory.objects.create(id=1, source="Hello")
        if created_budget:
            budget = Budget.objects.create(
                id=1,
                name="Test Budget",
                user=user,
                income_category=income_category,
                date=datetime(2022, 1, 1, 0, 0, tzinfo=timezone.utc).isoformat(),
                amount=100,
            )
            return budget
        else:
            return logger.info("Create dummy data sucessfully")

    def get_the_data_from_json_file(self, json_file_path):
        with open(json_file_path, "r") as json_file:
            data = json.load(json_file)
        if "date" not in data:
            return data
        date_obj = datetime.fromisoformat(data["date"].replace("Z", "+00:00")).replace(
            tzinfo=timezone.utc
        )
        data["date"] = date_obj.isoformat()
        return data
