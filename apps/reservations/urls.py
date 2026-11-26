from django.urls import path

from . import views


app_name = "reservations"

urlpatterns = [
    path("adicionar/", views.add_reservation, name="add_reservation"),
]