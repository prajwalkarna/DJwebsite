from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect, render

from .forms import LoginForm, RegisterForm


def register_view(request):
    form = RegisterForm()

    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
    return render(request, "accounts/register.html", {"form": form})


def login_view(request):
    form = LoginForm()

    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data["email"]
            password = form.cleaned_data["password"]
            user = authenticate(request, username=email, password=password)

            if user is not None:
                login(request, user)
                return redirect("dashboard")
            else:
                form.add_error(None, "Invalid email or password")
    return render(request, "accounts/login.html", {"form": form})


def logout_view(request):
    logout(request)
    return redirect("login")


# Create your views here.
