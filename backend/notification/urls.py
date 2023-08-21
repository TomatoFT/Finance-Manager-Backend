from django.urls import path

from . import views

urlpatterns = [
    path(
        "get_all_notifications_data/",
        views.get_all_notifications_data,
        name="get_all_notifications_data",
    ),
    path(
        "get_notification_data/",
        views.get_notification_data,
        name="get_notification_data",
    ),
    path(
        "add_notification_data/",
        views.add_notification_data,
        name="add_notification_data",
    ),
    # path("update/<str:content>/", views.update_data),
    # path("delete/<str:content>/", views.delete_data),
]
