from django            import forms
from .models           import Inspection
from django.utils.html import format_html
from core.forms        import BaseForm

class InspectionForm(BaseForm):

    class Meta:
        model   = Inspection
        exclude = ()
