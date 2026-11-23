from django.urls import path

from . import views


app_name = "protections"

urlpatterns = [
    path("adicionar/", views.add_protection, name="add_protection"),
    path("listar/", views.list_protections, name="list_protections"),
    path("editar/<int:id>/", views.edit_protection, name="edit_protection"),
    path("excluir/<int:id>/", views.delete_protection, name="delete_protection"),
]