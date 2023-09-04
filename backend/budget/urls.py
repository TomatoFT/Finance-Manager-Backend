from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from . import views

urlpatterns = [
    # Budget CRUD handling
    path("", views.BudgetManagement.as_view(), name="Budget Management"),
    path(
        "<int:budget_id>",
        views.BudgetDetailManagement.as_view(),
        name="Budget Detail Management",
    ),
    # Income Category CRUD Handling
    path(
        "income",
        views.IncomeCategoryManagement.as_view(),
        name="get_all_income_categories",
    ),
    path(
        "income/<int:income_category_id>",
        views.IncomeDetailCategoryManagement.as_view(),
        name="get_income_category_details",
    ),
]
urlpatterns = format_suffix_patterns(urlpatterns)
