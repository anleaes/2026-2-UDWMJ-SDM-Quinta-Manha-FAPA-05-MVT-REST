from django.urls import path

from . import views


app_name = "clients"

urlpatterns = [
    path("adicionar/", views.add_client, name="add_client"),
    path("listar/", views.list_clients, name="list_clients"),
]