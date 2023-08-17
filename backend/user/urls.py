from django.urls import path

from . import views

urlpatterns = [
    # User CRUD handling
    path(
        "get_all_users_informations",
        views.get_all_users_informations,
        name="get_all_users_informations",
    ),
    path(
        "get_user/<int:user_id>",
        views.get_user,
        name="get_user",
    ),
    path(
        "add_user",
        views.add_user,
        name="add_user",
    ),
    path(
        "update_user/<int:user_id>",
        views.update_user,
        name="update_user",
    ),
    path(
        "delete_user/<int:user_id>",
        views.delete_user,
        name="delete_user",
    ),
]
