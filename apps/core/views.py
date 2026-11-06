from django.shortcuts import render
from django.http      import HttpRequest, HttpResponse

# Create your views here.

def home(request: HttpRequest) -> HttpResponse:
    template_name = "core/home.html"
    context       = {}
    return render(request, template_name, context)
