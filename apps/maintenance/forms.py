from django     import forms
from .models    import Maintenance
from core.forms import BaseForm

class MaintenanceForm(BaseForm):

    class Meta:
        model   = Maintenance
        exclude = ()
