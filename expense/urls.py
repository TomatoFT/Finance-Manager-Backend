from django.urls import path
from expense import views

urlpatterns = [
    path("", views.ExpenseManagement.as_view(), name="expense_management"),
    path(
        "<int:expense_id>",
        views.ExpenseDetailManagement.as_view(),
        name="expense_detail_management",
    ),
    path(
        "category",
        views.ExpenseCategoryManagement.as_view(),
        name="expense_category_management",
    ),
    path(
        "category/<int:expense_category_id>",
        views.ExpenseCategoryDetailManagement.as_view(),
        name="expense_category_detail_management",
    ),
]
