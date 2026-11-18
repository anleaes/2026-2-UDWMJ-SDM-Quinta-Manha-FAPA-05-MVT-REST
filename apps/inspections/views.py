from django.shortcuts               import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.http                    import HttpRequest, HttpResponse
from .forms                         import InspectionForm
from .models                        import Inspection

# Create your views here.
@login_required
def add_inspection(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        form = InspectionForm(request.POST, request.FILES)
        if form.is_valid():
            f = form.save(commit = False)
            f.save()
            form.save_m2m()
            return redirect("inspections:list_inspections")

    template_name = "inspections/add_inspection.html"
    form          = InspectionForm()
    context       = {
        "form": form
    }
    return render(request, template_name, context)

@login_required
def list_inspections(request: HttpRequest) -> HttpResponse:
    template_name = "inspections/list_inspections.html"
    inspections   = Inspection.objects.select_related("employee").all()
    # inspections   = Inspection.objects.select_related("reservation", "employee").all()
    context = {
        "inspections" : inspections,
    }
    return render(request, template_name, context)
