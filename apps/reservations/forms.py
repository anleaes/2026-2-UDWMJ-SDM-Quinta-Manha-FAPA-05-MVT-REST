from django import forms
from django.db.models import Q

from clients.models import Client
from employees.models import Employee
from protections.models import Protection
from vehicles.models import Vehicle
from .models import Reservation

class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = [
            "client", "vehicle", "employee", "protection",
            "expected_pickup", "expected_return", "notes",
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields["client"].queryset = Client.objects.filter(is_active=True)
        self.fields["vehicle"].queryset = Vehicle.objects.filter(
            is_active=True
        ).select_related("vehicle_model")
        self.fields["employee"].queryset = Employee.objects.filter(isactive=True)
        self.fields["protection"].queryset = Protection.objects.filter(
            Q(is_active=True) | Q(pk=self.instance.protection_id)
        )

        for name in ("expected_pickup", "expected_return"):
            self.fields[name] = forms.DateTimeField(
                label=self.fields[name].label,
                input_formats=["%d/%m/%Y %H:%M", "%Y-%m-%dT%H:%M"],
                widget=forms.DateTimeInput(
                    format="%d/%m/%Y %H:%M",
                    attrs={"placeholder": "DD/MM/AAAA HH:MM", "maxlength": 16},
                ),
            )