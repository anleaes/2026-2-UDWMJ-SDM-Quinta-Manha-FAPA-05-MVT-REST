from django.urls import path
from .           import views

app_name = "inspections"

urlpatterns = [
    path("adicionar/", views.add_inspection, name = "add_inspection"),
    path("listar/", views.list_inspections, name = "list_inspections"),
    path("editar/<int:id>/", views.edit_inspection, name = "edit_inspection"),
]
