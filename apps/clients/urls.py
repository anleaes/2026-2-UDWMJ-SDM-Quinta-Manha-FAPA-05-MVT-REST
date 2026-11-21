from django.urls import path

from . import views


app_name = "clients"

urlpatterns = [
    path("adicionar/", views.add_client, name="add_client"),
    path("listar/", views.list_clients, name="list_clients"),
    path("editar/<int:id>/", views.edit_client, name="edit_client"),
]