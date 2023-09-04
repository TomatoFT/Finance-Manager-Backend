from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from . import views

urlpatterns = [
    # Expense CRUD perform
    path("", views.ExpenseManagement.as_view(), name="Expense Management"),
    path(
        "<int:expense_id>",
        views.ExpenseDetailManagement.as_view(),
        name="Expense Detail Management",
    ),
    path(
        "category",
        views.ExpenseCategoryManagement.as_view(),
        name="Expense Category Management",
    ),
    path(
        "category/<int:expense_category_id>",
        views.ExpenseCategoryDetailManagement.as_view(),
        name="Expense Category Detail Management",
    ),
]
urlpatterns = format_suffix_patterns(urlpatterns)
