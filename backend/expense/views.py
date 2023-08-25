from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Expense, ExpenseCategory
from .serializers import ExpenseCategorySerializer, ExpenseSerializer


# CRUD ON BUDGET
@api_view(["GET"])
def get_all_expenses(request):
    expenses_list = Expense.objects.all()
    serializers = ExpenseSerializer(expenses_list, many=True)
    return Response(serializers.data)


@api_view(["GET"])
def get_expense_details(request, expense_id):
    expense_details = Expense.objects.filter(id=expense_id)
    serializers = ExpenseSerializer(expense_details, many=True)
    return Response(serializers.data)


@api_view(["POST"])
def add_expense_details(request):
    serializers = ExpenseSerializer(data=request.data)
    if serializers.is_valid():
        serializers.save()
    return Response(serializers.data)


@api_view(["PUT"])
def update_expense_data(request, expense_id):
    expense_data = Expense.objects.get(id=expense_id)
    data = ExpenseSerializer(instance=expense_data, data=request.data)
    print("DATA:", data)
    if data.is_valid():
        data.save()
        return Response(data.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(["DELETE", "GET"])
def delete_expense_data(request, expense_id):
    item = get_object_or_404(Expense, id=expense_id)
    item.delete()
    return redirect(reverse("get_all_expenses"))


# CRUD ON EXPENSE CATEGORY TABLE
@api_view(["GET"])
def get_all_expense_categories(request):
    expense_categories_list = ExpenseCategory.objects.all()
    serializers = ExpenseCategorySerializer(expense_categories_list, many=True)
    return Response(serializers.data)


@api_view(["GET"])
def get_expense_category_details(request, expense_category_id):
    expense_category = ExpenseCategory.objects.filter(id=expense_category_id)
    serializers = ExpenseCategorySerializer(expense_category, many=True)
    return Response(serializers.data)


@api_view(["POST"])
def add_expense_category_details(request):
    serializers = ExpenseCategorySerializer(data=request.data)
    if serializers.is_valid():
        serializers.save()
    return Response(serializers.data)


@api_view(["PUT"])
def update_expense_category(request, expense_category_id):
    expense_category = ExpenseCategory.objects.get(id=expense_category_id)
    data = ExpenseCategorySerializer(instance=expense_category, data=request.data)
    print("DATA:", data)
    if data.is_valid():
        data.save()
        return Response(data.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(["DELETE", "GET"])
def delete_expense_category(request, expense_category_id):
    item = get_object_or_404(ExpenseCategory, id=expense_category_id)
    item.delete()
    return redirect(reverse("get_all_expense_categories"))
