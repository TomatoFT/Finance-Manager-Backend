import logging

from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Budget, IncomeCategory
from .serializers import BudgetSerializer, IncomeCategorySerializer


class BudgetManagement(APIView):
    def get(self, request):
        budgets_list = Budget.objects.all()
        serializers = BudgetSerializer(budgets_list, many=True)
        return Response(serializers.data)

    def post(self, request):
        logger = logging.getLogger(__name__)
        budget_data = preprocess_budget_data(request)
        serializers = BudgetSerializer(data=budget_data)
        try:
            serializers.is_valid(raise_exception=True)
            serializers.save()
            return Response(serializers.data)
        except ValidationError as e:
            error_message = e.detail
            return Response(error_message, status=status.HTTP_400_BAD_REQUEST)


class BudgetDetailManagement(APIView):
    def get(self, request, budget_id):
        budget_details = Budget.objects.filter(id=budget_id)
        serializers = BudgetSerializer(budget_details, many=True)
        return Response(serializers.data)

    def put(self, request, budget_id):
        budget_data = Budget.objects.get(id=budget_id)
        serializers = BudgetSerializer(instance=budget_data, data=request.data)
        try:
            serializers.is_valid(raise_exception=True)
            serializers.save()
            return Response(serializers.data)
        except ValidationError as e:
            error_message = e.detail
            return Response(error_message, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, budget_id):
        item = get_object_or_404(Budget, id=budget_id)
        item.delete()
        return Response(status=status.HTTP_200_OK)


def preprocess_budget_data(request):
    budget_data = {
        "name": request.data["name"],
        "amount": request.data["amount"],
        "always_notify": request.data["always_notify"],
        "user": request.data["user"],
        "income_category": request.data["income_category"],
    }

    return budget_data


class IncomeCategoryManagement(APIView):
    def get(self, request):
        income_categories_list = IncomeCategory.objects.all()
        serializers = IncomeCategorySerializer(income_categories_list, many=True)
        return Response(serializers.data)

    def post(self, request):
        serializers = IncomeCategorySerializer(data=request.data)
        try:
            serializers.is_valid(raise_exception=True)
            serializers.save()
            return Response(serializers.data)
        except ValidationError as e:
            error_message = e.detail
            return Response(error_message, status=status.HTTP_400_BAD_REQUEST)


class IncomeDetailCategoryManagement(APIView):
    def get(self, request, income_category_id):
        income_category = IncomeCategory.objects.filter(id=income_category_id)
        serializers = IncomeCategorySerializer(income_category, many=True)
        return Response(serializers.data)

    def put(self, request, income_category_id):
        income_category = IncomeCategory.objects.get(id=income_category_id)
        serializers = IncomeCategorySerializer(
            instance=income_category, data=request.data
        )
        try:
            serializers.is_valid(raise_exception=True)
            serializers.save()
            return Response(serializers.data)
        except ValidationError as e:
            error_message = e.detail
            return Response(error_message, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, income_category_id):
        item = get_object_or_404(IncomeCategory, id=income_category_id)
        item.delete()
        return Response(status=status.HTTP_202_ACCEPTED)
