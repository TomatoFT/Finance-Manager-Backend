"""
Expense Management API

This module contains API views for managing expenses and expense categories.

"""

from django.shortcuts import get_object_or_404
from expense.models import Expense, ExpenseCategory
from expense.serializers import ExpenseCategorySerializer, ExpenseSerializer
from rest_framework import status
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from rest_framework.views import APIView


class ExpenseManagement(APIView):
    """
    API view for managing expenses.

    This view allows retrieving all expenses, creating a new expense, and handling
    individual expense details.

    """

    def get(self, request):
        """
        Retrieve all expenses.

        This method retrieves all expenses and returns a serialized representation of the data.

        Returns:
            Response: Serialized data of all expenses.

        """

        expenses_list = Expense.objects.all()
        serializer = ExpenseSerializer(expenses_list, many=True)
        return Response(serializer.data)

    def post(self, request):
        """
        Create a new expense.

        This method creates a new expense based on the provided data and returns the serialized
        representation of the created expense.

        Args:
            request (Request): The HTTP request object.

        Returns:
            Response: Serialized data of the created expense and
            the suitable status for the request.

        """

        serializer = ExpenseSerializer(data=request.data)
        try:
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except ValidationError as e:
            error_message = e.detail
            return Response(error_message, status=status.HTTP_400_BAD_REQUEST)


class ExpenseDetailManagement(APIView):
    """
    API view for managing individual expense details.

    This view allows retrieving, updating, and deleting individual expense details.

    """

    def get(self, request, expense_id):
        """
        Retrieve a specific expense.

        This method retrieves a specific expense based on the provided expense ID and returns
        a serialized representation of the expense.

        Args:
            request (Request): The HTTP request object.
            expense_id (int): The ID of the expense to retrieve.

        Returns:
            Response: Serialized data of the retrieved expense.

        """

        expense_details = Expense.objects.filter(id=expense_id)
        serializer = ExpenseSerializer(expense_details, many=True)
        return Response(serializer.data)

    def put(self, request, expense_id):
        """
        Update a specific expense.

        This method updates a specific expense based on the provided expense ID and data, and
        returns the serialized representation of the updated expense.

        Args:
            request (Request): The HTTP request object.
            expense_id (int): The ID of the expense to update.

        Returns:
            Response: Serialized data of the updated expense and
            the suitable status for the request.

        """

        expense_data = Expense.objects.get(id=expense_id)
        serializer = ExpenseSerializer(instance=expense_data, data=request.data)
        try:
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except ValidationError as e:
            error_message = e.detail
            return Response(error_message, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, expense_id):
        """
        Delete a specific expense.

        This method deletes a specific expense based on the provided expense ID.

        Args:
            request (Request): The HTTP request object.
            expense_id (int): The ID of the expense to delete.

        Returns:
            Response: Empty response with status code 204 (No Content)
            or status code 404 if the data not found in database .

        """

        matched_expense = get_object_or_404(Expense, id=expense_id)
        matched_expense.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ExpenseCategoryManagement(APIView):
    """
    API view for managing expense categories.

    This view allows retrieving all expense categories, creating a new expense category, and
    handling individual expense category details.

    """

    def get(self, request):
        """
        Retrieve all expense categories.

        This method retrieves all expense categories and returns a serialized representation
        of the data.

        Returns:
            Response: Serialized data of all expense categories.

        """

        expense_categories_list = ExpenseCategory.objects.all()
        serializer = ExpenseCategorySerializer(expense_categories_list, many=True)
        return Response(serializer.data)

    def post(self, request):
        """
        Create a new expense category.

        This method creates a new expense category based on the provided data and returns the
        serialized representation of the created expense category.

        Args:
            request (Request): The HTTP request object.

        Returns:
            Response: Serialized data of the created expense category.

        """

        serializer = ExpenseCategorySerializer(data=request.data)
        try:
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except ValidationError as e:
            error_message = e.detail
            return Response(error_message, status=status.HTTP_400_BAD_REQUEST)


class ExpenseCategoryDetailManagement(APIView):
    """
    API view for managing individual expense category details.

    This view allows retrieving, updating, and deleting individual expense category details.

    """

    def get(self, request, expense_category_id):
        """
        Retrieve a specific expense category.

        This method retrieves a specific expense category based on the provided expense category ID
        and returns a serialized representation of the expense category.

        Args:
            request (Request): The HTTP request object.
            expense_category_id (int): The ID of the expense category to retrieve.

        Returns:
            Response: Serialized data of the retrieved expense category.

        """

        expense_category = ExpenseCategory.objects.filter(id=expense_category_id)
        serializer = ExpenseCategorySerializer(expense_category, many=True)
        return Response(serializer.data)

    def put(self, request, expense_category_id):
        """
        Update a specific expense category.

        This method updates a specific expense category based on the provided expense category ID
        and data, and returns the serialized representation of the updated expense category.

        Args:
            request (Request): The HTTP request object.
            expense_category_id (int): The ID of the expense category to update.

        Returns:
            Response: Serialized data of the updated expense category and
            the suitable status for the request.

        """

        expense_category = ExpenseCategory.objects.get(id=expense_category_id)
        serializer = ExpenseCategorySerializer(
            instance=expense_category, data=request.data
        )
        try:
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_204_NO_CONTENT)
        except ValidationError as e:
            error_message = e.detail
            return Response(error_message, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, expense_category_id):
        """
        Delete a specific expense category.

        This method deletes a specific expense category based on the provided expense category ID.

        Args:
            request (Request): The HTTP request object.
            expense_category_id (int): The ID of the expense category to delete.

        Returns:
            Response: Empty response with status code 204 (No Content) or
            status code 404 if the data is not found in the database.

        """

        matched_category = get_object_or_404(ExpenseCategory, id=expense_category_id)
        matched_category.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
