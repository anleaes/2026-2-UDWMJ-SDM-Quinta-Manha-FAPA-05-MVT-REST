from django.urls import path
from . import views

app_name = "categories"

urlpatterns = [
    path("adicionar/", views.add_category, name="add_category"),
    path("listar/", views.list_categories, name="list_categories"),
    path("editar/<int:id>/", views.edit_category, name="edit_category"),
]