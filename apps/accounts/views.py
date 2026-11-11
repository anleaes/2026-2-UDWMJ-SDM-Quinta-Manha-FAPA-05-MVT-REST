from django.shortcuts               import render, redirect
from django.contrib.auth.models     import User
from django.contrib.auth            import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms      import PasswordChangeForm
from .forms                         import UserForm, UserChangeInformationForm

# Create your views here.
def add_user(request: HttpRequest) -> HttpResponse:
    template_name = "accounts/add_user.html"
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            f = form.save(commit = False)
            f.set_password(f.password)
            f.save()
            return redirect("accounts:user_login")
        return redirect("accounts:add_user")
    form    = UserForm()
    context = {
        "form" : form,
    }
    return render(request, template_name, context)
