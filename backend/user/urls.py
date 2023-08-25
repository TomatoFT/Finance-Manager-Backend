from django.urls import path

from . import views

urlpatterns = [
    # User CRUD handling
    path(
        "",
        views.get_all_users_informations,
        name="get_all_users_informations",
    ),
    path(
        "<int:user_id>",
        views.get_user,
        name="get_user",
    ),
    path(
        "",
        views.add_user,
        name="add_user",
    ),
    path(
        "<int:user_id>",
        views.update_user,
        name="update_user",
    ),
    path(
        "<int:user_id>",
        views.delete_user,
        name="delete_user",
    ),
]
