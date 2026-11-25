from django import forms
from clients.models import Client
from .models import CNH

class CNHForm(forms.ModelForm):
    class Meta:
        model = CNH
        fields = ["client", "number", "category", "expiration_date", "document"]
        widgets = {
            "number": forms.TextInput(attrs={"inputmode": "numeric"}),
            "expiration_date": forms.DateInput(
                format="%d/%m/%Y",
                attrs={
                    "type": "text",
                    "placeholder": "DD/MM/AAAA",
                    "maxlength": 10,
                },
            ),
            "document": forms.FileInput(),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["expiration_date"].input_formats = ["%d/%m/%Y", "%Y-%m-%d"]
        client_field = self.fields["client"]

        if self.instance.pk:
            client_field.queryset = Client.objects.filter(pk=self.instance.client_id)
            client_field.disabled = True
        else:
            client_field.queryset = Client.objects.filter(
                cnh__isnull=True
            ).order_by("name", "pk")

    def clean_category(self):
        return self.cleaned_data["category"].upper()