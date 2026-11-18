from django.urls import path
from .           import views

app_name = "inspections"

urlpatterns = [
    path("adicionar/", views.add_inspection, name = "add_inspection"),
]
