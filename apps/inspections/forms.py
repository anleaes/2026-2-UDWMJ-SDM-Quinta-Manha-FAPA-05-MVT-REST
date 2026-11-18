from django            import forms
from .models           import Inspection
from django.utils.html import format_html

class InspectionForm(forms.ModelForm):
    # NOTE: Remove `:` suffix for labels
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.label_suffix = ""

    class Meta:
        model   = Inspection
        exclude = ()
