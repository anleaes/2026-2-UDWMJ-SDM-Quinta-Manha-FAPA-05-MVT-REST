from django.contrib.auth.decorators import login_required
from django.db.models import ProtectedError
from django.http import HttpRequest, HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from core.forms import Forms
from .forms import ClientForm
from .models import Client

# Create your views here.

pages = Forms.pages(Client, ClientForm, "clients", "Client")

def _save_client(request, instance=None):
    form = ClientForm(request.POST, instance=instance)

    if form.is_valid():
        form.save()
        return redirect(pages.templates.url)

    return render(request, pages.templates.add, {"form": form})

@login_required
def add_client(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        return _save_client(request)

    return pages.add(request)

@login_required
def list_clients(request: HttpRequest) -> HttpResponse:
    return pages.list(request)