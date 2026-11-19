from django.urls import path
from . import views

app_name = "brands"

urlpatterns = [
    path("adicionar/", views.add_brand, name="add_brand"),
]