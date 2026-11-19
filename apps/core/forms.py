from django.shortcuts import render, get_object_or_404, redirect
from django.http      import HttpRequest, HttpResponse
from dataclasses      import dataclass
from django.conf      import settings
from django           import forms

@dataclass
class Templates():
    def __init__(self, name: str, singular_name: str):
        self.directory = name
        self.url       = f"{name}:list_{name}"
        self.list      = f"{name}/list_{name}.html"
        self.add       = f"{name}/add_{singular_name}.html"
        if settings.DEBUG:
            print(f"Generating templates for `{name}`")
            print(f"    Directory -> {self.directory}")
            print(f"    URL       -> {self.url}")
            print(f"    List      -> {self.list}")
            print(f"    Add       -> {self.add}")
            print("")

class Forms():
    def __init__(self, Model, ModelForm, name: str, singular_name: str):
        self.Model     = Model
        self.ModelForm = ModelForm
        self.templates = Templates(name, singular_name)

    def add(self, request: HttpRequest) -> HttpResponse:
        if request.method == "POST":
            form = self.ModelForm(request.POST, request.FILES)
            if form.is_valid():
                f = form.save(commit = False)
                f.save()
                form.save_m2m()
                return redirect(self.templates.url)
        context = { "form" : self.ModelForm() }
        return render(request, self.templates.add, context)

    def list(self, request: HttpRequest) -> HttpResponse:
        context = { self.templates.directory : self.Model.objects.filter() }
        return render(request, self.templates.list, context)

    def edit(self, request: HttpRequest, id: int) -> HttpResponse:
        instance = get_object_or_404(self.Model, id = id)
        if request.method == "POST":
            form = self.ModelForm(request.POST, request.FILES, instance = instance)
            if form.is_valid():
                form.save()
                return redirect(self.templates.url)
        context = { "form" : self.ModelForm(instance = instance) }
        return render(request, self.templates.add, context)

    def delete(self, request: HttpRequest, id: int) -> HttpResponse:
        instance = self.Model.objects.get(id = id)
        instance.delete()
        return redirect(self.templates.url)

class BaseForm(forms.ModelForm):
    # NOTE: Remove `:` suffix for labels
    def __init__(self, *args, **kwargs):
        kwargs.setdefault("label_suffix", "")
        super().__init__(*args, **kwargs)
