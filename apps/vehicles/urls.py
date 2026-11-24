from django.urls import path
from . import views

app_name = "vehicles"

urlpatterns = [
    path("adicionar/", views.add_vehicle, name="add_vehicle"),
    path("listar/", views.list_vehicles, name="list_vehicles"),
    path("editar/<int:id>/", views.edit_vehicle, name="edit_vehicle"),
]