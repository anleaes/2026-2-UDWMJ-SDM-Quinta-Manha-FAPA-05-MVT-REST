from django.urls import path
from .           import views

app_name = "maintenance"

urlpatterns = [
    path("adicionar/", views.add_maintenance, name = "add_maintenance"),
    path("listar/", views.list_maintenance, name = "list_maintenance"),
    path("editar/<int:id>/", views.edit_maintenace, name = "edit_maintenace"),
]
