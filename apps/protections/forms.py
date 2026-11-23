from django import forms
from .models import Protection

class ProtectionForm(forms.ModelForm):
    class Meta:
        model = Protection
        fields = ['name', 'description', 'daily_rate', 'deductible', 'is_active']
        localized_fields = ['daily_rate', 'deductible']