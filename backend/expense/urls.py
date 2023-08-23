from django.urls import path

from . import views

urlpatterns = [
    # Budget CRUD handling
    path("", views.get_all_expenses, name="get_all_expenses"),
    path(
        "<int:expense_id>",
        views.get_expense_details,
        name="get_expense_details",
    ),
    path("add", views.add_expense_details, name="add_expense_data"),
    path(
        "update/<int:expense_id>",
        views.update_expense_data,
        name="update_expense_data",
    ),
    path(
        "delete/<int:expense_id>",
        views.delete_expense_data,
        name="delete_expense_data",
    ),
    # Expense Category CRUD Handling
    path(
        "expense_category",
        views.get_all_expense_categories,
        name="get_all_expense_categories",
    ),
    path(
        "expense_category/<int:expense_category_id>",
        views.get_expense_category_details,
        name="get_expense_category_details",
    ),
    path(
        "expense_category/add",
        views.add_expense_category_details,
        name="add_expense_category_details",
    ),
    path(
        "expense_category/update/<int:expense_category_id>",
        views.update_expense_category,
        name="update_expense_category",
    ),
    path(
        "expense_category/delete/<int:expense_category_id>",
        views.delete_expense_category,
        name="delete_expense_category",
    ),
]
