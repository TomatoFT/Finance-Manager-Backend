from django.shortcuts import get_object_or_404
from expense.models import Expense, ExpenseCategory
from expense.serializers import ExpenseCategorySerializer, ExpenseSerializer
from rest_framework import status
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from rest_framework.views import APIView


class ExpenseManagement(APIView):
    def get(self, request):
        expenses_list = Expense.objects.all()
        serializer = ExpenseSerializer(expenses_list, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ExpenseSerializer(data=request.data)
        try:
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except ValidationError as e:
            error_message = e.detail
            return Response(error_message, status=status.HTTP_400_BAD_REQUEST)


class ExpenseDetailManagement(APIView):
    def get(self, request, expense_id):
        expense_details = Expense.objects.filter(id=expense_id)
        serializer = ExpenseSerializer(expense_details, many=True)
        return Response(serializer.data)

    def put(self, request, expense_id):
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
        matched_expense = get_object_or_404(Expense, id=expense_id)
        matched_expense.delete()
        return Response(status=status.HTTP_202_ACCEPTED)


# CRUD ON EXPENSE CATEGORY TABLE
class ExpenseCategoryManagement(APIView):
    def get(self, request):
        expense_categories_list = ExpenseCategory.objects.all()
        serializer = ExpenseCategorySerializer(expense_categories_list, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ExpenseCategorySerializer(data=request.data)
        try:
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except ValidationError as e:
            error_message = e.detail
            return Response(error_message, status=status.HTTP_400_BAD_REQUEST)


class ExpenseCategoryDetailManagement(APIView):
    def get(self, request, expense_category_id):
        expense_category = ExpenseCategory.objects.filter(id=expense_category_id)
        serializer = ExpenseCategorySerializer(expense_category, many=True)
        return Response(serializer.data)

    def put(self, request, expense_category_id):
        expense_category = ExpenseCategory.objects.get(id=expense_category_id)
        serializer = ExpenseCategorySerializer(
            instance=expense_category, data=request.data
        )
        try:
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except ValidationError as e:
            error_message = e.detail
            return Response(error_message, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, expense_category_id):
        matched_category = get_object_or_404(ExpenseCategory, id=expense_category_id)
        matched_category.delete()
        return Response(status=status.HTTP_202_ACCEPTED)
