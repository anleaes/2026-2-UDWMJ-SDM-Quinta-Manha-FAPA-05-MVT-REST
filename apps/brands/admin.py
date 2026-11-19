from django.contrib import admin
from .models import Brand
# Register your models here.

@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "name",
        "country_origin",
        "isactive",
    ]

    search_fields = [
        "name",
        "country_origin",
    ]

    list_filter = ["isactive"]