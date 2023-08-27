from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Expense, ExpenseCategory
from .serializers import ExpenseCategorySerializer, ExpenseSerializer


class ExpenseManagement(APIView):
    def get(self, request):
        expenses_list = Expense.objects.all()
        serializers = ExpenseSerializer(expenses_list, many=True)
        return Response(serializers.data)

    def post(self, request):
        serializers = ExpenseSerializer(data=request.data)
        try:
            serializers.is_valid(raise_exception=True)
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        except ValidationError as e:
            error_message = e.detail
            return Response(error_message, status=status.HTTP_400_BAD_REQUEST)


class ExpenseDetailManagement(APIView):
    def get(self, request, expense_id):
        expense_details = Expense.objects.filter(id=expense_id)
        serializers = ExpenseSerializer(expense_details, many=True)
        return Response(serializers.data)

    def put(self, request, expense_id):
        expense_data = Expense.objects.get(id=expense_id)
        serializers = ExpenseSerializer(instance=expense_data, data=request.data)
        try:
            serializers.is_valid(raise_exception=True)
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        except ValidationError as e:
            error_message = e.detail
            return Response(error_message, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, expense_id):
        item = get_object_or_404(Expense, id=expense_id)
        item.delete()
        return Response(status=status.HTTP_202_ACCEPTED)


# CRUD ON EXPENSE CATEGORY TABLE
class ExpenseCategoryManagement(APIView):
    def get(self, request):
        expense_categories_list = ExpenseCategory.objects.all()
        serializers = ExpenseCategorySerializer(expense_categories_list, many=True)
        return Response(serializers.data)

    def post(self, request):
        serializers = ExpenseCategorySerializer(data=request.data)
        try:
            serializers.is_valid(raise_exception=True)
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        except ValidationError as e:
            error_message = e.detail
            return Response(error_message, status=status.HTTP_400_BAD_REQUEST)


class ExpenseCategoryDetailManagement(APIView):
    def get(self, request, expense_category_id):
        expense_category = ExpenseCategory.objects.filter(id=expense_category_id)
        serializers = ExpenseCategorySerializer(expense_category, many=True)
        return Response(serializers.data)

    def put(self, request, expense_category_id):
        expense_category = ExpenseCategory.objects.get(id=expense_category_id)
        serializers = ExpenseCategorySerializer(
            instance=expense_category, data=request.data
        )
        try:
            serializers.is_valid(raise_exception=True)
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        except ValidationError as e:
            error_message = e.detail
            return Response(error_message, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, expense_category_id):
        item = get_object_or_404(ExpenseCategory, id=expense_category_id)
        item.delete()
        return Response(status=status.HTTP_202_ACCEPTED)
