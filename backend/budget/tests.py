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
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create(
            id=1, username="abc", password="abc", email="abc@a.com", phone=121112222111
        )
        self.income_category = IncomeCategory.objects.create(id=1, source="Hello")
        self.budget = Budget.objects.create(
            name="Test Budget",
            user=self.user,
            income_category=self.income_category,
            date=datetime(2022, 1, 1, 0, 0, tzinfo=timezone.utc).isoformat(),
            amount=3000000,
        )
        self.budget_data = {
            "name": "sssss",
            "amount": 1500000,
            "always_notify": True,
            "user": 1,
            "income_category": 1,
        }

    def test_get_budgets(self):
        url = reverse("budget_management")
        response = self.client.get(url)
        expenses = Budget.objects.all()
        serializer = BudgetSerializer(expenses, many=True)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

    def test_create_budget(self):
        url = reverse("budget_management")
        data = self.budget_data
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        budget = Budget.objects.last()
        self.assertEqual(budget.name, data["name"])
        self.assertEqual(budget.income_category.id, data["income_category"])
        self.assertEqual(budget.user.id, data["user"])
        self.assertEqual(budget.always_notify, data["always_notify"])
        self.assertEqual(budget.amount, data["amount"])
        self.assertEqual(Budget.objects.count(), 2)

    def test_create_budget_with_invalid_data(self):
        url = reverse("budget_management")
        data = self.budget_data
        data["amount"] = -45555
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(Budget.objects.count(), 1)

    def test_update_budget_with_invalid_data(self):
        url = reverse("budget_detail_management", args=[self.budget.id])
        data = self.budget_data
        data["amount"] = -51111
        response = self.client.put(url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_update_budget(self):
        url = reverse("budget_detail_management", args=[self.budget.id])
        data = self.budget_data
        data["amount"] = 7000000  # Update valid data
        response = self.client.put(url, data)
        # Perform Unit Testing
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.budget.refresh_from_db()
        self.assertEqual(self.budget.name, data["name"])
        self.assertEqual(self.budget.income_category.id, data["income_category"])
        self.assertEqual(self.budget.user.id, data["user"])
        self.assertEqual(self.budget.always_notify, data["always_notify"])
        self.assertEqual(self.budget.amount, data["amount"])

    def test_delete_budget(self):
        url = reverse("budget_detail_management", args=[self.budget.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Budget.objects.count(), 0)
