from django.contrib import admin
from .models import Brand
# Register your models here.

@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "name",
        "country_origin",
        "is_active",
    ]

    search_fields = [
        "name",
        "country_origin",
    ]

    list_filter = ["is_active"]