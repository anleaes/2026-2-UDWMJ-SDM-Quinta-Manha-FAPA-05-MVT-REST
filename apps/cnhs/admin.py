from django.contrib import admin
from .forms import CNHForm
from .models import CNH
# Register your models here.
@admin.register(CNH)
class CNHAdmin(admin.ModelAdmin):
    form = CNHForm
    list_display = ("number", "client", "category", "expiration_date")
    list_filter = ("category", "expiration_date")
    search_fields = ("number", "client__name", "client__cpf")
    list_select_related = ("client",)