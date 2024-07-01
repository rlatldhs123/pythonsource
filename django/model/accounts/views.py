from django.shortcuts import render, redirect

from .forms import UserForm

from django.contrib.auth import authenticate, login, logout

# Create your views here.


def register(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("index")

    else:
        form = UserForm()

    return render(request, "register.html", {"form": form})
