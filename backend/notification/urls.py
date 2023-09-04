from django.urls import path

from . import views

urlpatterns = [
    path(
        "",
        views.NotificationManagement.as_view(),
        name="Notification Management",
    ),
    path(
        "<int:notification_id>",
        views.NotificationDetailManagement.as_view(),
        name="Notification Detail Management",
    ),
]
