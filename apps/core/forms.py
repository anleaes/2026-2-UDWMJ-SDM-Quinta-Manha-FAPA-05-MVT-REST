from django.shortcuts import render, get_object_or_404, redirect
from django.http      import HttpRequest, HttpResponse

class Templates():
    def __init__(self, directory: str, list: str, add: str):
        self.directory = directory
        self.url       = f"{directory}:{list}"
        self.list      = f"{directory}/{list}.html"
        self.add       = f"{directory}/{add}.html"

class Forms():
    def __init__(self, Class, Form, template_directory: str, template_list: str, template_add: str):
        self.Class     = Class
        self.Form      = Form
        self.templates = Templates(template_directory, template_list, template_add)

    def add(self, request: HttpRequest) -> HttpResponse:
        if request.method == "POST":
            form = self.Form(request.POST, request.FILES)
            if form.is_valid():
                f = form.save(commit = False)
                f.save()
                form.save_m2m()
                return redirect(self.templates.url)
        context = { "form" : self.Form() }
        return render(request, self.templates.add, context)

    def list(self, request: HttpRequest) -> HttpResponse:
        context = { self.templates.directory : self.Class.objects.filter() }
        return render(request, self.templates.list, context)

    def edit(self, request: HttpRequest, id: int) -> HttpResponse:
        instance = get_object_or_404(self.Class, id = id)
        if request.method == "POST":
            form = self.Form(request.POST, request.FILES, instance = instance)
            if form.is_valid():
                form.save()
                return redirect(self.templates.url)
        context = { "form" : self.Form(instance = instance) }
        return render(request, self.templates.add, context)

    def delete(self, request: HttpRequest, id: int) -> HttpResponse:
        instance = self.Class.objects.get(id = id)
        instance.delete()
        return redirect(self.templates.url)
