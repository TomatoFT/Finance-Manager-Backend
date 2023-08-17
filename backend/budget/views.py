from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Budget, IncomeCategory
from .serializers import BudgetSerializer, IncomeCategorySerializer


# CRUD ON BUDGET
@api_view(["GET"])
def get_all_budgets(request):
    budgets_list = Budget.objects.all()
    serializers = BudgetSerializer(budgets_list, many=True)
    return Response(serializers.data)


@api_view(["GET"])
def get_budget_details(request, budget_id):
    budget_details = Budget.objects.filter(budget_id=budget_id)
    serializers = BudgetSerializer(budget_details, many=True)
    return Response(serializers.data)


@api_view(["POST"])
def add_budget_details(request):
    serializers = BudgetSerializer(data=request.data)
    if serializers.is_valid():
        serializers.save()
    return Response(serializers.data)


@api_view(["PUT"])
def update_budget_data(request, budget_id):
    budget_data = Budget.objects.get(budget_id=budget_id)
    data = BudgetSerializer(instance=budget_data, data=request.data)
    print("DATA:", data)
    if data.is_valid():
        data.save()
        return Response(data.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(["DELETE", "GET"])
def delete_budget_data(request, budget_id):
    item = get_object_or_404(Budget, budget_id=budget_id)
    item.delete()
    return redirect(reverse("get_all_budgets"))


# CRUD ON INCOME CATEGORY TABLE
@api_view(["GET"])
def get_all_income_categories(request):
    income_categories_list = IncomeCategory.objects.all()
    serializers = IncomeCategorySerializer(income_categories_list, many=True)
    return Response(serializers.data)


@api_view(["GET"])
def get_income_category_details(request, income_category_id):
    income_category = IncomeCategory.objects.filter(
        income_category_id=income_category_id
    )
    serializers = IncomeCategorySerializer(income_category, many=True)
    return Response(serializers.data)


@api_view(["POST"])
def add_income_category_details(request):
    serializers = IncomeCategorySerializer(data=request.data)
    if serializers.is_valid():
        serializers.save()
    return Response(serializers.data)


@api_view(["PUT"])
def update_income_category(request, income_category_id):
    income_category = IncomeCategory.objects.get(income_category_id=income_category_id)
    data = IncomeCategorySerializer(instance=income_category, data=request.data)
    print("DATA:", data)
    if data.is_valid():
        data.save()
        return Response(data.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(["DELETE", "GET"])
def delete_income_category(request, income_category_id):
    item = get_object_or_404(IncomeCategory, income_category_id=income_category_id)
    item.delete()
    return redirect(reverse("get_all_income_categories"))
