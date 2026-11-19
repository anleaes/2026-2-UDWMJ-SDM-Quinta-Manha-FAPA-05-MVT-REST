from django.shortcuts               import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.http                    import HttpRequest, HttpResponse
from .forms                         import EmployeeForm
from .models                        import Employee
from core.forms                     import Forms

form = Forms(Model         = Employee,
             ModelForm     = EmployeeForm,
             name          = "employees",
             singular_name = "employee")

# Create your views here.
@login_required
def add_employee(request: HttpRequest) -> HttpResponse:
    return form.add(request)

@login_required
def list_employees(request: HttpRequest) -> HttpResponse:
    return form.list(request)

@login_required
def edit_employee(request: HttpRequest, id: int) -> HttpResponse:
    return form.edit(request, id)

@login_required
def delete_employee(request: HttpRequest, id: int) -> HttpResponse:
    return form.delete(request, id)
