from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpRequest
from django.shortcuts import render, redirect

from core.forms import Forms
from .forms import VehicleModelForm
from .models import VehicleModel
# Create your views here.

pages = Forms.pages(VehicleModelForm, VehicleModel, "vehicleModels", "vehicleModel")

def __save_vehicle_model(request, instance=None):
    form = VehicleModelForm(request.POST, instance=instance)

    if form.is_valid():
        form.save()
        return redirect(pages.templates.url)

    return render(request, pages.templates.save, {"form": form})

@login_required
def add_vehicle_model(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        return __save_vehicle_model(request)

    return pages.add(request)


