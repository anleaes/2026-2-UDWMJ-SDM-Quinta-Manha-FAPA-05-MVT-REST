from django.shortcuts               import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.http                    import HttpRequest, HttpResponse
from .models                        import Payment
from .forms                         import PaymentForm
from core.forms                     import Forms

# Create your views here.
form = Forms(Model         = Payment,
             ModelForm     = PaymentForm,
             name          = "payments",
             singular_name = "payment")

# Create your views here.
@login_required
def add_payment(request: HttpRequest) -> HttpResponse:
    return form.add(request)

@login_required
def list_payments(request: HttpRequest) -> HttpResponse:
    return form.list(request, related_fields = ["employee", "inspection"])

@login_required
def edit_payment(request: HttpRequest, id: int) -> HttpResponse:
    return form.edit(request, id)

