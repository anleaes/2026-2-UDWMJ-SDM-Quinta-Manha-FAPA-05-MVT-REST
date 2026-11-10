from django.shortcuts import render, get_object_or_404, redirect
from .forms           import EmployeeForm
from .models          import Employee

# Create your views here.
def add_employee(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        form = EmployeeForm(request.POST)
        if form.is_valid():
            f = form.save(commit = False)
            f.save()
            form.save_m2m()
            return redirect("employees:list_employees")

    template_name = "employees/add_employee.html"
    form          = EmployeeForm()
    context       = {
        "form": form
    }
    return render(request, template_name, context)

def list_employees(request: HttpRequest) -> HttpResponse:
    template_name = "employees/list_employees.html"
    employees     = Employee.objects.filter()
    context = {
        "employees" : employees,
    }
    return render(request, template_name, context)
