from django.urls import path
from .           import views

app_name = "payments"

urlpatterns = [
    path("adicionar/", views.add_payment, name = "add_payment"),
    path("listar/", views.list_payments, name = "list_payments"),
    path("editar/<int:id>/", views.edit_payment, name = "edit_payment"),
    path("excluir/<int:id>/", views.delete_payment, name = "delete_payment"),
]
