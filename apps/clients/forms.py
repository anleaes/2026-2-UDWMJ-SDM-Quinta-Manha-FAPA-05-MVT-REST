from django import forms

from .models import Client


class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ["name", "cpf", "email", "phone", "birth_date", "is_active"]
        widgets = {
            "cpf": forms.TextInput(attrs={"inputmode": "numeric"}),
            "birth_date": forms.DateInput(
                format="%Y-%m-%d",
                attrs={"type": "date"},
            ),
        }