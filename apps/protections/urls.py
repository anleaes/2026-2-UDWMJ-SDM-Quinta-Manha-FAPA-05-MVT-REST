from django.urls import path

from . import views


app_name = "protections"

urlpatterns = [
    path("adicionar/", views.add_protection, name="add_protection"),
]