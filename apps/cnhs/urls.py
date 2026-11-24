from django.urls import path
from . import views

app_name = "cnhs"

urlpatterns = [
    path("adicionar/", views.add_cnh, name="add_cnh"),
    path("listar/", views.list_cnhs, name="list_cnhs"),
    path("arquivo/<int:id>/", views.download_cnh, name="download_cnh"),
    path("editar/<int:id>/", views.edit_cnh, name="edit_cnh"),
    path("excluir/<int:id>/", views.delete_cnh, name="delete_cnh"),
]