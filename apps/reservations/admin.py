from django.contrib import admin, messages
from django.core.exceptions import ValidationError
from django.shortcuts import redirect

from .forms import ReservationForm
from .models import Reservation
from .views import confirm_reservation


# Register your models here.

@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    form = ReservationForm
    list_display = ("id", "client", "vehicle", "expected_pickup", "status", "estimated_total")
    list_filter = ("status",)
    search_fields = ("client__name", "vehicle__plate")
    list_select_related = ("client", "vehicle__vehicle_model")
    readonly_fields = (
        "created_at", "status", "contracted_daily_rate",
        "contracted_protection_rate", "contracted_deductible", "estimated_total",
    )
    actions = ["cancel_confirmed"]

    def save_model(self, request, obj, form, change):
        confirm_reservation(obj)

    def changeform_view(self, request, object_id=None, form_url="", extra_context=None):
        try:
            return super().changeform_view(request, object_id, form_url, extra_context)
        except ValidationError as error:
            self.message_user(request, " ".join(error.messages), level=messages.ERROR)
            return redirect(request.path)

    @admin.action(description="Cancelar reservas confirmadas", permissions=["change"])
    def cancel_confirmed(self, request, queryset):
        count = queryset.filter(
            status=Reservation.Status.CONFIRMED
        ).update(status=Reservation.Status.CANCELLED)
        self.message_user(request, f"Reservas canceladas: {count}.")

    def has_delete_permission(self, request, obj=None):
        return False