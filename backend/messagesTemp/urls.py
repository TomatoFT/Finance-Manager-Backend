from django.urls import path

from . import views

urlpatterns = [
    path("get_data", views.get_data, name="get_data"),
    path("add/", views.add_data),
    path("update/<str:content>/", views.update_data),
    path("delete/<str:content>/", views.delete_data),
]
