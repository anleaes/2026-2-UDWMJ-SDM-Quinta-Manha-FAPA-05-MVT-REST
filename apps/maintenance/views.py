from django.shortcuts               import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.http                    import HttpRequest, HttpResponse
from .forms                         import MaintenanceForm
from .models                        import Maintenance

# Create your views here.
@login_required
def add_maintenance(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        form = MaintenanceForm(request.POST)
        if form.is_valid():
            f = form.save(commit = False)
            f.save()
            form.save_m2m()
            return redirect("maintenance:list_maintenance")

    template_name = "maintenance/add_maintenance.html"
    form          = MaintenanceForm()
    context       = {
        "form": form
    }
    return render(request, template_name, context)

@login_required
def list_maintenance(request: HttpRequest) -> HttpResponse:
    template_name = "maintenance/list_maintenance.html"
    maintenance     = Maintenance.objects.select_related("vehicle", "employee").all()
    context = {
        "maintenance" : maintenance,
    }
    return render(request, template_name, context)

@login_required
def edit_maintenance(request: HttpRequest, id: int) -> HttpResponse:
    maintenance = get_object_or_404(Employee, id = id)
    if request.method == "POST":
        form = MaintenanceForm(request.POST, instance = maintenance)
        if form.is_valid():
            form.save()
            return redirect("maintenance:list_maintenance")

    template_name = "maintenance/add_maintenance.html"
    form          = MaintenanceForm(instance = maintenance)
    context       = {
        "form": form
    }
    return render(request, template_name, context)

@login_required
def delete_maintenance(request: HttpRequest, id: int) -> HttpResponse:
    maintenance = Maintenance.objects.get(id = id)
    maintenance.delete()
    return redirect("maintenance:list_maintenance")
