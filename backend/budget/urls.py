from django.urls import path

from . import views

urlpatterns = [
    # Budget CRUD handling
    path("", views.get_all_budgets, name="get_all_budgets"),
    path(
        "<int:budget_id>",
        views.get_budget_details,
        name="get_budget_details",
    ),
    path("add", views.add_budget_details, name="add_budget_data"),
    path(
        "update/<int:budget_id>",
        views.update_budget_data,
        name="update_budget_data",
    ),
    path(
        "delete/<int:budget_id>",
        views.delete_budget_data,
        name="delete_budget_data",
    ),
    # Income Category CRUD Handling
    path(
        "income_category",
        views.get_all_income_categories,
        name="get_all_income_categories",
    ),
    path(
        "income_category/<int:income_category_id>",
        views.get_income_category_details,
        name="get_income_category_details",
    ),
    path(
        "income_category/add",
        views.add_income_category_details,
        name="add_income_category_details",
    ),
    path(
        "income_category/update/<int:income_category_id>",
        views.update_income_category,
        name="update_income_category",
    ),
    path(
        "income_category/delete/<int:income_category_id>",
        views.delete_income_category,
        name="delete_income_category",
    ),
]
