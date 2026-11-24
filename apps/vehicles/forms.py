from django import forms
from .models import Vehicle

class VehicleForm(forms.ModelForm):
    class Meta:
        model = Vehicle
        fields = ["vehicle_model", "plate", "renavam", "year", "color", "current_km", "photo", "is_active"]
    def clean_current_km(self):
        km = self.cleaned_data["current_km"]

        if self.instance.pk and km < self.instance.current_km:
            raise forms.ValidationError("A quilometragem atual não pode ser menor que a quilometragem anterior.")

        return km