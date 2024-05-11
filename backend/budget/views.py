"""
Budget Management API

This module contains API views for managing budgets and income categories.

"""
import logging

from budget.models import Budget, IncomeCategory
from budget.serializers import BudgetSerializer, IncomeCategorySerializer
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

logger = logging.getLogger(__name__)

class BudgetManagement(APIView):
    """
    API view for managing budgets.

    This view allows retrieving all budgets, creating a new budget, and handling
    individual budget details.

    """

    permission_classes = [IsAuthenticated]

    def get(self, request):
        """
        Retrieve all budgets.

        This method retrieves all budgets and returns a serialized representation of the data.

        Returns:
            Response: Serialized data of all budgets.

        """

        budgets_list = Budget.objects.all()
        serializer = BudgetSerializer(budgets_list, many=True)
        logger.info("{} -- {}".format(request.user, request.auth))
        return Response(serializer.data)

    def post(self, request):
        """
        Create a new budget.

        This method creates a new budget based on the provided data and returns the serialized
        representation of the created budget.

        Args:
            request (Request): The HTTP request object.

        Returns:
            Response: Serialized data of the created budget.

        """
        data = request.data
        data["user"] = request.user.id
        serializer = BudgetSerializer(data=data)
        try:
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except ValidationError as error_message:
            return Response(error_message.detail, status=status.HTTP_400_BAD_REQUEST)


class BudgetDetailManagement(APIView):
    """
    API view for managing individual budget details.

    This view allows retrieving, updating, and deleting individual budget details.

    """

    def get(self, request, budget_id):
        """
        Retrieve a specific budget.

        This method retrieves a specific budget based on the provided budget ID and returns
        a serialized representation of the budget.

        Args:
            request (Request): The HTTP request object.
            budget_id (int): The ID of the budget to retrieve.

        Returns:
            Response: Serialized data of the retrieved budget.

        """

        budget_details = Budget.objects.filter(id=budget_id)
        serializer = BudgetSerializer(budget_details, many=True)
        return Response(serializer.data)

    def put(self, request, budget_id):
        """
        Update a specific budget.

        This method updates a specific budget based on the provided budget ID and data, and
        returns the serialized representation of the updated budget.

        Args:
            request (Request): The HTTP request object.
            budget_id (int): The ID of the budget to update.

        Returns:
            Response: Serialized data of the updated budget and
            the suitable status for the request.

        """

        budget_data = get_object_or_404(Budget, id=budget_id)
        serializer = BudgetSerializer(instance=budget_data, data=request.data)
        try:
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        except ValidationError as error_message:
            return Response(error_message.detail, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, budget_id):
        """
        Delete a specific budget.

        This method deletes a specific budget based on the provided budget ID.

        Args:
            request (Request): The HTTP request object.
            budget_id (int): The ID of the budget to delete.

        Returns:
            Response: Empty response with status code 204 (No Content).

        """

        matched_budget = get_object_or_404(Budget, id=budget_id)
        matched_budget.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class IncomeCategoryManagement(APIView):
    """
    API view for managing income categories.

    This view allows retrieving all income categories, creating a new income category, and
    handling individual income category details.

    """

    def get(self, request):
        """
        Retrieve all income categories.

        This method retrieves all income categories and returns a serialized representation
        of the data.

        Returns:
            Response: Serialized data of all income categories.

        """

        income_categories_list = IncomeCategory.objects.all()
        serializer = IncomeCategorySerializer(income_categories_list, many=True)
        return Response(serializer.data)

    def post(self, request):
        """
        Create a new income category.

        This method creates a new income category based on the provided data and returns the
        serialized representation of the created income category.

        Args:
            request (Request): The HTTP request object.

        Returns:
            Response: Serialized data of the created income category and
            the suitable status for the request.

        """

        serializer = IncomeCategorySerializer(data=request.data)
        try:
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except ValidationError as error_message:
            return Response(error_message.detail, status=status.HTTP_400_BAD_REQUEST)


class IncomeDetailCategoryManagement(APIView):
    """
    API view for managing individual income category details.

    This view allows retrieving, updating, and deleting individual income category details.

    """

    def get(self, request, income_category_id):
        """
        Retrieve a specific income category.

        This method retrieves a specific income category based on the provided income category ID
        and returns a serialized representation of the income category.

        Args:
            request (Request): The HTTP request object.
            income_category_id (int): The ID of the income category to retrieve.

        Returns:
            Response: Serialized data of the retrieved income category.

        """

        income_category = IncomeCategory.objects.filter(id=income_category_id)
        serializer = IncomeCategorySerializer(income_category, many=True)
        return Response(serializer.data)

    def put(self, request, income_category_id):
        """
        Update a specific income category.

        This method updates a specific income category based on the provided income category ID
        and data, and returns the serialized representation of the updated income category.

        Args:
            request (Request): The HTTP request object.
            income_category_id (int): The ID of the income category to update.

        Returns:
            Response: Serialized data of the updated income category and
            the suitable status for the request.

        """

        income_category = get_object_or_404(IncomeCategory, id=income_category_id)
        serializer = IncomeCategorySerializer(
            instance=income_category, data=request.data
        )
        try:
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except ValidationError as error_message:
            return Response(error_message.detail, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, income_category_id):
        """
        Delete a specific income category.

        This method deletes a specific income category based on the provided income category ID.

        Args:
            request (Request): The HTTP request object.
            income_category_id (int): The ID of the income category to delete.

        Returns:
            Response: Empty response with status code 204 (No Content)
            and status code 404 if the data is not found in database.

        """

        matched_income_category = get_object_or_404(IncomeCategory, id=income_category_id)
        matched_income_category.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
