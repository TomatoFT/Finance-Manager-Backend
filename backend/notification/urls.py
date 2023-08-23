from django.urls import path

from . import views

urlpatterns = [
    path(
        "",
        views.get_all_notifications_data,
        name="get_all_notifications_data",
    ),
    # path(
    #     "/",
    #     views.get_notification_data,
    #     name="get_notification_data",
    # ),
    path(
        "add/",
        views.add_notification_data,
        name="add_notification_data",
    ),
    # path("update/<str:content>/", views.update_data),
    # path("delete/<str:content>/", views.delete_data),
]
