from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from . import views

urlpatterns = [
    # Budget CRUD handling
    path("", views.BudgetManagement.as_view()),
    path("<int:budget_id>", views.BudgetDetailManagement.as_view()),
    # # Income Category CRUD Handling
    # path(
    #     "income_category",
    #     views.get_all_income_categories,
    #     name="get_all_income_categories",
    # ),
    # path(
    #     "income_category/<int:income_category_id>",
    #     views.get_income_category_details,
    #     name="get_income_category_details",
    # ),
    # path(
    #     "income_category",
    #     views.add_income_category_details,
    #     name="add_income_category_details",
    # ),
    # path(
    #     "income_category/<int:income_category_id>",
    #     views.update_income_category,
    #     name="update_income_category",
    # ),
    # path(
    #     "income_category/<int:income_category_id>",
    #     views.delete_income_category,
    #     name="delete_income_category",
    # ),
]
urlpatterns = format_suffix_patterns(urlpatterns)
