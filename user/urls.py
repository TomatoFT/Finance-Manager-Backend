from django.urls import path
from user import views

urlpatterns = [
    # User CRUD handling
    path(
        "",
        views.UserManagement.as_view(),
        name="user_management",
    ),
    path(
        "<int:user_id>",
        views.UserDetailManagement.as_view(),
        name="user_detail_management",
    ),
]
