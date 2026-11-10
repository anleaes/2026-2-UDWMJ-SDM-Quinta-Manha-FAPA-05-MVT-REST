from django.urls import path
from .           import views

app_name = "employees"

urlpatterns = [
    path("adicionar/", views.add_employee, name = "add_employee"),
    path("listar/", views.list_employees, name = "list_employees"),
]
