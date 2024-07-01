from django.shortcuts import render, redirect
from .forms import UserForm

from django.contrib.auth import authenticate, login, logout


def index(request):
    return render(request, "index.html")


def register(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("index")

    else:
        form = UserForm()

    return render(request, "register.html", {"form": form})


def common_login(request):

    if request.method == "POST":
        # 입력값 가지고 오기
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("index")

    return render(request, "login.html")


def common_logout(request):
    logout(request)
    return redirect("index")
