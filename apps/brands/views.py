from django.contrib.auth.decorators import login_required
from django.db.models import ProtectedError

from core.forms import *

from .forms import BrandForm
from .models import Brand
# Create your views here.

form = Forms(
    Brand,
    BrandForm,
    "brands",
    "brand",
)

@login_required
def add_brand(request: HttpRequest) -> HttpResponse:
    return form.add(request)

@login_required
def list_brands(request: HttpRequest) -> HttpResponse:
    return form.list(request)

@login_required
def edit_brand(request: HttpRequest, id: int) -> HttpResponse:
    return form.edit(request, id)

@login_required
def delete_brand(request: HttpRequest, id: int) -> HttpResponse:
    brand = Brand.objects.get(id = id)
    error = None

    if request.method == "POST":
        try:
            return form.delete(request, id)

        except ProtectedError:
            error = "Não é possível excluir a marca, pois existem veículos associados a ela!"

    context = { "brand" : brand, "error" : error }
    return render(request, "brands/delete_brand.html", context)
