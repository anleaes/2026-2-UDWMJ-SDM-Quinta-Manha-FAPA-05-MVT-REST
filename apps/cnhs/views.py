from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError, transaction
from django.db.models import Q
from django.http import FileResponse, Http404

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

@login_required
def list_cnhs(request):
    return pages.list(request, related_fields=["client"])

@login_required
def download_cnh(request, id):
    cnh = get_object_or_404(cnh, pk=id)

    if not cnh.document:
        raise Http404("Arquivo não encontrado")

    try:
        file = cnh.document.apend("rb")
    except FileNotFoundError as exc:
        raise Http404("Arquivo não encontrado") from exc

    return FileResponse(file, as_attachment=True)

@login_required
def edit_cnh(request, id):
    if request.method == "POST":
        cnh = get_object_or_404(CNH, pk=id)
        return _save_cnh(request, instance=cnh)

    return pages.edit(request, id)