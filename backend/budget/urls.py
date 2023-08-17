from django.urls import path

from . import views

urlpatterns = [
    # Budget CRUD handling
    path("get_all_budgets_data", views.get_all_budgets, name="get_all_budgets"),
    path(
        "get_detail_budget_data/<int:budget_id>",
        views.get_budget_details,
        name="get_budget_details",
    ),
    path("add_budget_data", views.add_budget_details, name="add_budget_data"),
    path(
        "update_budget_data/<int:budget_id>",
        views.update_budget_data,
        name="update_budget_data",
    ),
    path(
        "delete_budget_data/<int:budget_id>",
        views.delete_budget_data,
        name="delete_budget_data",
    ),
    # Income Category CRUD Handling
    path(
        "get_all_income_categories",
        views.get_all_income_categories,
        name="get_all_income_categories",
    ),
    path(
        "get_income_category_details/<int:income_category_id>",
        views.get_income_category_details,
        name="get_income_category_details",
    ),
    path(
        "add_income_category_details",
        views.add_income_category_details,
        name="add_income_category_details",
    ),
    path(
        "update_income_category/<int:income_category_id>",
        views.update_income_category,
        name="update_income_category",
    ),
    path(
        "delete_income_category/<int:income_category_id>",
        views.delete_income_category,
        name="delete_income_category",
    ),
]
