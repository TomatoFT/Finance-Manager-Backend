from budget import views
from django.urls import path

urlpatterns = [
    # Budget CRUD handling
    path("", views.BudgetManagement.as_view(), name="budget_management"),
    path(
        "<int:budget_id>",
        views.BudgetDetailManagement.as_view(),
        name="budget_detail_management",
    ),
    # Income Category CRUD Handling
    path(
        "income",
        views.IncomeCategoryManagement.as_view(),
        name="income_category_management",
    ),
    path(
        "income/<int:income_category_id>",
        views.IncomeDetailCategoryManagement.as_view(),
        name="income_detail_category_management",
    ),
]
