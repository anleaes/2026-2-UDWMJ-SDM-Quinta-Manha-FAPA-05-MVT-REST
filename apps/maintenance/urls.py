from django.urls import path
from .           import views

app_name = "maintenance"

urlpatterns = [
    path("adicionar/", views.add_maintenance, name = "add_maintenance"),
]
