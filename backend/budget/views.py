from budget.models import Budget, IncomeCategory
from budget.serializers import BudgetSerializer, IncomeCategorySerializer
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from rest_framework.views import APIView


class BudgetManagement(APIView):
    def get(self, request):
        budgets_list = Budget.objects.all()
        serializer = BudgetSerializer(budgets_list, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = BudgetSerializer(data=request.data)
        try:
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except ValidationError as error_message:
            return Response(error_message.detail, status=status.HTTP_400_BAD_REQUEST)


class BudgetDetailManagement(APIView):
    def get(self, request, budget_id):
        budget_details = Budget.objects.filter(id=budget_id)
        serializer = BudgetSerializer(budget_details, many=True)
        return Response(serializer.data)

    def put(self, request, budget_id):
        budget_data = get_object_or_404(Budget, id=budget_id)
        serializer = BudgetSerializer(instance=budget_data, data=request.data)
        try:
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        except ValidationError as error_message:
            return Response(error_message.detail, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, budget_id):
        matched_budget = get_object_or_404(Budget, id=budget_id)
        matched_budget.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class IncomeCategoryManagement(APIView):
    def get(self, request):
        income_categories_list = IncomeCategory.objects.all()
        serializer = IncomeCategorySerializer(income_categories_list, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = IncomeCategorySerializer(data=request.data)
        try:
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except ValidationError as error_message:
            return Response(error_message.detail, status=status.HTTP_400_BAD_REQUEST)


class IncomeDetailCategoryManagement(APIView):
    def get(self, request, income_category_id):
        income_category = IncomeCategory.objects.filter(id=income_category_id)
        serializer = IncomeCategorySerializer(income_category, many=True)
        return Response(serializer.data)

    def put(self, request, income_category_id):
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
        matched_budghet = get_object_or_404(IncomeCategory, id=income_category_id)
        matched_budghet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
