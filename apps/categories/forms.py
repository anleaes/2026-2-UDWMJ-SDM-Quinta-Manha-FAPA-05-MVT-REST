from django import forms

from .models import Category


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ["name", "description", "default_daily_rate", "is_active"]
        localized_fields = ["default_daily_rate"]