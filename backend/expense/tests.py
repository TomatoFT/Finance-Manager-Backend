import json
from datetime import datetime, timezone

from budget.models import Budget, IncomeCategory
from django.test import TestCase
from django.urls import reverse
from expense.models import Expense, ExpenseCategory
from expense.serializers import ExpenseSerializer
from rest_framework import status
from rest_framework.test import APIClient
from user.models import User


class ExpenseManagementTests(TestCase):
    CREATE_TEST_PATH = "expense/test/create_expense_test.json"
    CREATE_INVALID_TEST_PATH = "expense/test/create_invalid_expense_test.json"
    UPDATE_TEST_PATH = "expense/test/update_expense_test.json"
    UPDATE_INVALID_TEST_PATH = "expense/test/update_invalid_expense_test.json"

    def setUp(self):
        self.client = APIClient()

    def test_get_expenses(self):
        url = reverse("Expense Management")
        response = self.client.get(url)
        expenses = Expense.objects.all()
        serializer = ExpenseSerializer(expenses, many=True)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

    def test_create_expense(self):
        url = reverse("Expense Management")
        _, budget = self.create_data()
        data = self.get_the_data_from_json_file(json_file_path=self.CREATE_TEST_PATH)
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        expense = Expense.objects.first()
        self.assertEqual(expense.budget.id, data["budget"])
        self.assertEqual(expense.expense_category.id, data["expense_category"])
        self.assertEqual(expense.date, datetime.fromisoformat(data["date"]))
        self.assertEqual(expense.amount, data["amount"])
        self.assertEqual(expense.budget.current_amount, budget.amount - data["amount"])

    def test_create_expense_with_invalid_data(self):
        url = reverse("Expense Management")
        data = self.get_the_data_from_json_file(
            json_file_path=self.CREATE_INVALID_TEST_PATH
        )
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(Expense.objects.count(), 0)

    def test_update_expense(self):
        expense_category, budget = self.create_data()
        expense = Expense.objects.create(
            id=1,
            budget=budget,
            expense_category=expense_category,
            date=datetime(2022, 1, 1, 0, 0, tzinfo=timezone.utc).isoformat(),
            amount=100,
        )
        url = reverse("Expense Detail Management", args=[expense.id])
        data = self.get_the_data_from_json_file(json_file_path=self.UPDATE_TEST_PATH)
        response = self.client.put(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        expense.refresh_from_db()
        self.assertEqual(expense.budget.id, data["budget"])
        self.assertEqual(expense.expense_category.id, data["expense_category"])
        self.assertEqual(expense.date.isoformat(), data["date"])
        self.assertEqual(expense.amount, data["amount"])
        self.assertEqual(budget.current_amount, budget.amount - data["amount"])

    def test_update_expense_with_invalid_data(self):
        expense_category, budget = self.create_data()
        expense = Expense.objects.create(
            budget=budget,
            expense_category=expense_category,
            date="2022-01-01T00:00:00Z",
            amount=100,
        )
        url = reverse("Expense Detail Management", args=[expense.id])
        data = self.get_the_data_from_json_file(
            json_file_path=self.UPDATE_INVALID_TEST_PATH
        )
        response = self.client.put(url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        expense.refresh_from_db()

    def test_delete_expense(self):
        expense_category, budget = self.create_data()
        expense = Expense.objects.create(
            budget=budget,
            expense_category=expense_category,
            date="2022-01-01T00:00:00Z",
            amount=100,
        )
        url = reverse("Expense Detail Management", args=[expense.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_202_ACCEPTED)
        self.assertEqual(Expense.objects.count(), 0)

    def create_data(self):
        user = User.objects.create(
            id=1, username="abc", password="abc", email="abc@a.com", phone=121112222111
        )
        income_category = IncomeCategory.objects.create(id=1, source="Hello")
        expense_category = ExpenseCategory.objects.create(id=1, name="Hello")
        budget = Budget.objects.create(
            id=1,
            user=user,
            name="Test expense",
            income_category=income_category,
            amount=500000,
            always_notify=True,
        )
        return expense_category, budget

    def get_the_data_from_json_file(self, json_file_path):
        with open(json_file_path, "r") as json_file:
            data = json.load(json_file)
        date_obj = datetime.fromisoformat(data["date"].replace("Z", "+00:00")).replace(
            tzinfo=timezone.utc
        )
        data["date"] = date_obj.isoformat()
        return data
