from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest
from django.contrib.auth.decorators import login_required

from core.forms import Forms
from .models import Category
from .forms import CategoryForm
# Create your views here.

pages = Forms(Category, CategoryForm, "categories", "category")

def _save_category(request, instance=None):
    form = CategoryForm(request.POST, instance=instance)

    if form.is_valid():
        form.save()

        return redirect(pages.templates.url)

    return render(request, pages.templates.add, {"form": form})


@login_required
def add_category(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        
        return _save_category(request)

    return pages.add(request)

@login_required
def list_categories(request: HttpRequest) -> HttpResponse:

    return pages.list(request)