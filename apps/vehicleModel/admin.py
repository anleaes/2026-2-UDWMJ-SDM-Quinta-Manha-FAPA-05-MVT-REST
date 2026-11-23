from django.contrib import admin
from .models import VehicleModel

# Register your models here.
@admin.register(VehicleModel)
class VehicleModelAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "brand", "category", "is_active")
    search_fields = ("name", "brand__name")
    list_filter = ("is_active", "category")