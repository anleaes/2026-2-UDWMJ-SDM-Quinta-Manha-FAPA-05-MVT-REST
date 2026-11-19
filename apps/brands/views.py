from django.contrib.auth.decorators import login_required

from core.forms import *

from .forms import BrandForm
from .models import Brand
# Create your views here.

form = Forms(
    Brand,
    BrandForm,
    "brands",
    "list_brands",
    "add_brand"
)

@login_required
def add_brand(request: HttpRequest) -> HttpResponse:
    return form.add(request)