from django.urls import path

from . import views

urlpatterns = [
    # Budget CRUD handling
    path("get_all_expenses_data", views.get_all_expenses, name="get_all_expenses"),
    path(
        "get_detail_expense_data/<int:expense_id>",
        views.get_expense_details,
        name="get_expense_details",
    ),
    path("add_expense_data", views.add_expense_details, name="add_expense_data"),
    path(
        "update_expense_data/<int:expense_id>",
        views.update_expense_data,
        name="update_expense_data",
    ),
    path(
        "delete_expense_data/<int:expense_id>",
        views.delete_expense_data,
        name="delete_expense_data",
    ),
    # Expense Category CRUD Handling
    path(
        "get_all_expense_categories",
        views.get_all_expense_categories,
        name="get_all_expense_categories",
    ),
    path(
        "get_expense_category_details/<int:expense_category_id>",
        views.get_expense_category_details,
        name="get_expense_category_details",
    ),
    path(
        "add_expense_category_details",
        views.add_expense_category_details,
        name="add_expense_category_details",
    ),
    path(
        "update_expense_category/<int:expense_category_id>",
        views.update_expense_category,
        name="update_expense_category",
    ),
    path(
        "delete_expense_category/<int:expense_category_id>",
        views.delete_expense_category,
        name="delete_expense_category",
    ),
]
