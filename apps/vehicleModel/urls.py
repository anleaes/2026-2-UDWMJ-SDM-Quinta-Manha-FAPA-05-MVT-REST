from django.urls import path
from . import views

app_name = 'vehicleModel'

urlpatterns = [
    path('adicionar/', views.add_vehicle_model, name='add_vehicle_model'),
    path('listar/', views.list_vehicle_models, name='list_vehicle_models'),
    path('editar/<int:id>/', views.edit_vehicle_model, name='edit_vehicle_model'),
    path('excluir/<int:id>/', views.delete_vehicle_model, name='delete_vehicle_model'),
]