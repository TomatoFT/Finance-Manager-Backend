"""
Expense Management Tests

This module contains unit tests for the expense management functionality.

"""

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
        """
        Set up the test environment.

        This method creates the necessary objects for testing the expense management functionality.

        """
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
        """
        Test the retrieval of expenses.

        This method tests the GET request to retrieve all expenses and compares the response
        with the expected serialized data.

        """
        url = reverse("expense_management")
        response = self.client.get(url)
        expenses = Expense.objects.all()
        serializer = ExpenseSerializer(expenses, many=True)
        # Perform Unit Test
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

    def test_create_expense(self):
        """
        Test the creation of an expense.

        This method tests the POST request to create a new expense and verifies that the
        expense is created with the correct data.

        """
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
        """
        Test the creation of an expense with invalid data.

        This method tests the POST request to create a new expense with invalid data and verifies
        that the appropriate error response is returned.

        """
        url = reverse("expense_management")
        data = self.handle_the_time_data(data=self.expense_data)
        data["amount"] = -2000  # Invalid data
        response = self.client.post(url, data)
        # Perform Unit Test
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.content,  b'{"amount":["Ensure this value is greater than or equal to 0."]}')
        self.assertEqual(Expense.objects.count(), 1)
        self.assertEqual(Expense.objects.all()[0].id, self.expense.id)

    def test_update_expense(self):
        """
        Test the update of an expense.

        This method tests the PUT request to update an existing expense and verifies that the
        expense is updated with the correct data.

        """
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
        """
        Test the update of an expense with invalid data.

        This method tests the PUT request to update an existing expense with invalid data and
        verifies that the appropriate error response is returned.

        """
        url = reverse("expense_detail_management", args=[self.expense.id])
        data = self.handle_the_time_data(data=self.expense_data)
        data["amount"] = -2000  # Invalid data
        # Perform Unit Test
        response = self.client.put(url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.content,  b'{"amount":["Ensure this value is greater than or equal to 0."]}')

    def test_delete_expense(self):
        """
        Test the deletion of an expense.

        This method tests the DELETE request to delete an existing expense and verifies that
        the expense is deleted successfully.

        """
        url = reverse("expense_detail_management", args=[self.expense.id])
        response = self.client.delete(url)
        # Perform Unit Test
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Expense.objects.count(), 0)

    def handle_the_time_data(self, data):
        """
        Handle the time data.

        This method converts the date string in the data dictionary to a datetime object with
        the correct timezone information.

        Args:
            data (dict): The data for the budget from user.

        Returns:
            dict: The updated data dictionary with the converted date.

        """
        date_obj = datetime.fromisoformat(data["date"].replace("Z", "+00:00")).replace(
            tzinfo=timezone.utc
        )
        data["date"] = date_obj.isoformat()
        return data
