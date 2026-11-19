from django     import forms
from .models    import Payment
from core.forms import BaseForm

class PaymentForm(BaseForm):

    class Meta:
        model   = Payment
        exclude = ("created_at",)
