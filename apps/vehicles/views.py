from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpRequest
from django.db import transaction
from django.db.models import ProtectedError

from core.forms import Forms
from .forms import VehicleForm
from .models import Vehicle

# Create your views here.

pages = Forms("vehicles", "Veículos", VehicleForm, Vehicle)

def _save_vehicle(request, instance=None):
    form = VehicleForm(request.POST, request.FILES, instance=instance)

    if form.is_valid():
        form.save()
        return redirect(pages.templates.url)
    return render(request, pages.templates.form, {"form": form})

@login_required
def add_vehicle(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        return _save_vehicle(request)
    return pages.add(request)

@login_required
def list_vehicles(request: HttpRequest) -> HttpResponse:
    return pages.list(request, related_fields=["vehicle_model__brand"])

@login_required
def edit_vehicle(request: HttpRequest, id: int) -> HttpResponse:
    if request.method == "POST":
        with transaction.atomic():
            vehicle = get_object_or_404(
                Vehicle.objects.select_for_update(),
                pk=id,
            )
            return _save_vehicle(request, instance=vehicle)

    return pages.edit(request, id)

@login_required
def delete_vehicle(request: HttpRequest, id: int) -> HttpResponse:
    vehicle = get_object_or_404(Vehicle, pk=id)
    error = None

    if request.method == "POST":
        try:
            vehicle.delete()
        except ProtectedError:
            error = "Este veículo está vinculado a outro registro e não pode ser excluído."
        else:
            return redirect(pages.templates.url)

    return render(request, "vehicles/delete_vehicle.html", {"vehicle": vehicle, "error": error})