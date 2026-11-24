from django.urls import path
from . import views

app_name = "cnhs"

urlpatterns = [
    path("adicionar/", views.add_cnh, name="add_cnh")
]