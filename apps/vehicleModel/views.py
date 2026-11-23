from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpRequest
from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import ProtectedError

from core.forms import Forms
from .forms import VehicleModelForm
from .models import VehicleModel
# Create your views here.

pages = Forms(VehicleModel, VehicleModelForm, "vehicleModel", "vehicleModel")
pages.templates.url = "vehicleModel:list_vehicle_models"


def _save_vehicle_model(request, instance=None):
    form = VehicleModelForm(request.POST, instance=instance)

    if form.is_valid():
        form.save()
        return redirect(pages.templates.url)

    return render(request, pages.templates.add, {"form": form})


@login_required
def add_vehicle_model(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        return _save_vehicle_model(request)
    return pages.add(request)


@login_required
def list_vehicle_models(request: HttpRequest) -> HttpResponse:
    return pages.list(request, related_fields=["brand", "category"])


@login_required
def edit_vehicle_model(request: HttpRequest, id: int) -> HttpResponse:
    if request.method == "POST":
        vehicle_model = get_object_or_404(VehicleModel, pk=id)
        return _save_vehicle_model(request, instance=vehicle_model)
    return pages.edit(request, id)


@login_required
def delete_vehicle_model(request: HttpRequest, id: int) -> HttpResponse:
    vehicle_model = get_object_or_404(VehicleModel, pk=id)
    error = None

    if request.method == "POST":
        try:
            vehicle_model.delete()
        except ProtectedError:
            error = "Não é possível excluir este modelo de veículo! Ele está associado a um ou mais veículos."
        else:
            return redirect(pages.templates.url)

    return render(
        request,
        "vehicleModel/delete_vehicleModel.html",
        {"vehicle_model": vehicle_model, "error": error},
    )