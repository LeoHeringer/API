from . import views
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path("/create-client", views.create_cliente, name="create-client"),
    path("/get-client", views.get_client, name="get-client"),
    path("/update-client", views.update_client, name="update-client"),
    path("/delete-client", views.delete_client, name="delete-client"),
]
