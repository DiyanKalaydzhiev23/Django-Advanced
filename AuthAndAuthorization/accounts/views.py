from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages


def login_fbv(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')

        messages.error(request, "Invalid username or password")

    return render(request, 'fbv/login.html')


def register_fbv(request: HttpRequest) -> HttpResponse:
    form = UserCreationForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        user = form.save()
        login(request, user)
        return redirect('home')

    return render(request, 'fbv/register.html', {"form": form})



def logout_fbv(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        logout(request)
        return redirect('home')
