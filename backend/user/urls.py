from django.urls import path

from . import views

urlpatterns = [
    # User CRUD handling
    path(
        "",
        views.UserManagement.as_view(),
        name="User Management",
    ),
    path(
        "<int:user_id>",
        views.UserDetailManagement.as_view(),
        name="User Detail Management",
    ),
]
