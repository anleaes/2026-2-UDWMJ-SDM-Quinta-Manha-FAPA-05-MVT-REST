from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError, transaction
from django.db.models import Q

from core.forms import Forms
from .forms import CNHForm
from .models import CNH
# Create your views here.

pages = Forms(CNH, CNHForm, "cnhs", "cnh")

def _save_cnh(request, instance=None):
    form = CNHForm(request.POST, request.FILES, instance=instance)

    if form.is_valid():
        try:
            with transaction.atomic():
                form.save()
        except IntegrityError:
            others = CNH.objects.all()
            if instance is not None:
                others = others.exclude(pk=instance.pk)

            conflict = Q(client=form.cleaned_data["client"]) | Q(
                number=form.cleaned_data["number"]
            )
            if not others.filter(conflict).exists():
                raise

            form.add_error(None, "Cliente ou Númro de CNH já possui cadastro.")
        else:
            return redirect(pages.templates.url)

    return render(request, pages.templates.add, {"form": form})


@login_required
def add_cnh(request):
    if request.method == "POST":
        return _save_cnh(request)

    return pages.add(request)
