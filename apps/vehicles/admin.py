from django.contrib import admin
from .models import Vehicle
from .forms import VehicleForm

# Register your models here.

@admin.register(Vehicle)
class VehicleAdmin(admin.ModelAdmin):
    form = VehicleForm
    list_display = ("vehicle_model", "plate", "renavam", "year", "color", "current_km", "is_active")
    list_filter = ("year", "is_active")