from . import views
from django.contrib import admin
from django.urls import path

urlpatterns = [
    # Clients
    path("/create-client", views.create_cliente, name="create_client"),
    path("/get-client", views.get_client, name="get_client"),
    path("/update-client", views.update_client, name="update_client"),
    path("/delete-client", views.delete_client, name="delete_client"),

    # Veihcles
    path("/create-vehicle-id", views.create_vehicle_id, name="create_vehicle_id")
]
