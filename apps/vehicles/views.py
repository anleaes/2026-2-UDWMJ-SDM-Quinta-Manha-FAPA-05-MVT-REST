from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpRequest

from core.forms import Forms
from .forms import VehicleForm
from .models import Vehicle

# Create your views here.

pages = Forms("vehicles", "Veículos", VehicleForm, Vehicle)

def __save_vehicle(request, instance=None):
    form = VehicleForm(request.POST, request.FILES, instance=instance)

    if form.is_valid():
        form.save()
        return redirect(pages.templates.url)
    return render(request, pages.templates.form, {"form": form})

@login_required
def add_vehicle(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        return __save_vehicle(request)
    return pages.add(request)

