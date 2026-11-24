from django.urls import path
from . import views

app_name = "vehicles"

urlpatterns = [
    path("adicionar/", views.add_vehicle, name="add_vehicle"),
]