import logging
from datetime import datetime, timezone

from budget.models import Budget, IncomeCategory
from django.test import TestCase
from django.urls import reverse
from expense.models import Expense, ExpenseCategory
from expense.serializers import ExpenseSerializer
from rest_framework import status
from rest_framework.test import APIClient
from user.models import User

logger = logging.getLogger(__name__)


class ExpenseManagementTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create(
            id=1, username="abc", password="abc", email="abc@a.com", phone=121112222111
        )
        self.income_category = IncomeCategory.objects.create(id=1, source="Hello")
        self.expense_category = ExpenseCategory.objects.create(id=1, name="Hello")
        self.budget = Budget.objects.create(
            id=1,
            user=self.user,
            name="Test expense",
            income_category=self.income_category,
            amount=500000,
            always_notify=True,
        )
        self.expense = Expense.objects.create(
            budget=self.budget,
            expense_category=self.expense_category,
            date="2022-01-01T00:00:00Z",
            amount=100,
        )
        self.expense_data = {
            "budget": 1,
            "expense_category": 1,
            "date": "2022-01-01T00:00:00Z",
            "amount": 400,
        }

    def test_get_expenses(self):
        url = reverse("expense_management")
        response = self.client.get(url)
        expenses = Expense.objects.all()
        serializer = ExpenseSerializer(expenses, many=True)
        # Perform Unit Test
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

    def test_create_expense(self):
        url = reverse("expense_management")
        data = self.handle_the_time_data(data=self.expense_data)
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        expense = Expense.objects.all().order_by("-id")[0]
        # Perform Unit Test
        self.assertEqual(Expense.objects.count(), 2)
        self.assertEqual(expense.budget.id, data["budget"])
        self.assertEqual(expense.expense_category.id, data["expense_category"])
        self.assertEqual(expense.date, datetime.fromisoformat(data["date"]))
        self.assertEqual(expense.amount, data["amount"])
        self.assertEqual(
            expense.budget.current_amount,
            self.budget.amount - self.expense.amount - data["amount"],
        )

    def test_create_expense_with_invalid_data(self):
        url = reverse("expense_management")
        data = self.handle_the_time_data(data=self.expense_data)
        data["amount"] = -2000  # Invalid data
        response = self.client.post(url, data)
        # Perform Unit Test
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        logger.warn(
            "Invalid data while performing POST method for create_expense function. {}".format(
                response.content
            )
        )
        self.assertEqual(Expense.objects.count(), 1)
        self.assertEqual(Expense.objects.all()[0].id, self.expense.id)

    def test_update_expense(self):
        url = reverse("expense_detail_management", args=[self.expense.id])
        data = self.handle_the_time_data(data=self.expense_data)
        response = self.client.put(url, data)
        expense = Expense.objects.get(id=self.expense.id)
        # Perform Unit Test
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(expense.budget.id, data["budget"])
        self.assertEqual(expense.expense_category.id, data["expense_category"])
        self.assertEqual(expense.date, datetime.fromisoformat(data["date"]))
        self.assertEqual(expense.amount, data["amount"])
        self.assertEqual(
            expense.budget.current_amount, self.budget.amount - data["amount"]
        )

    def test_update_expense_with_invalid_data(self):
        url = reverse("expense_detail_management", args=[self.expense.id])
        data = self.handle_the_time_data(data=self.expense_data)
        data["amount"] = -2000  # Invalid data
        # Perform Unit Test
        response = self.client.put(url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        logger.warn(
            "Invalid data while performing PUT method for update_expense function. {}".format(
                response.content
            )
        )

    def test_delete_expense(self):
        url = reverse("expense_detail_management", args=[self.expense.id])
        response = self.client.delete(url)
        # Perform Unit Test
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Expense.objects.count(), 0)

    def handle_the_time_data(self, data):
        date_obj = datetime.fromisoformat(data["date"].replace("Z", "+00:00")).replace(
            tzinfo=timezone.utc
        )
        data["date"] = date_obj.isoformat()
        return data
