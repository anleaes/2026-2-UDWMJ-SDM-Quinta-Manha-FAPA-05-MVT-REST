from django import forms
from .models import VehicleModel

class VehicleModelForm(forms.ModelForm):
    class Meta:
        model = VehicleModel
        fields = ['brand', 'category', 'name', 'engine', 'transmission', 'seats', 'average_km_per_liter', 'is_active']
        localized_fields = ['average_km_per_liter']