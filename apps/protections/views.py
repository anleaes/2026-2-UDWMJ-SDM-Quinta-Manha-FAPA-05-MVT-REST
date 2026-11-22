from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.db.models import ProtectedError
from django.http import HttpResponse, HttpRequest

from core.forms import Forms
from .forms import ProtectionForm
from .models import Protection

# Create your views here.

pages = Forms(Protection, ProtectionForm, "protections", "protection")

def _save_protection(request, instance=None):
    form = ProtectionForm(request.POST, instance=instance)

    if form.is_valid():
        form.save()
        return redirect(pages.templates.url)

    return render(request, pages.templates.add, {"form": form})


@login_required
def add_protection(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        return _save_protection(request)

    return pages.add(request)


@login_required
def list_protections(request: HttpRequest) -> HttpResponse:
    return pages.list(request)


@login_required
def edit_protection(request: HttpRequest, id: int) -> HttpResponse:
    if request.method == "POST":
        protection = get_object_or_404(Protection, pk=id)
        return _save_protection(request, instance=protection)

    return pages.edit(request, id)