from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib.auth.decorators import user_passes_test, login_required, permission_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.mixins import UserPassesTestMixin
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import CreateView

from accounts.forms import SetUnusablePasswordForm

UserModel = get_user_model()


class RegisterView(UserPassesTestMixin, CreateView):
    form_class = UserCreationForm
    model = UserModel
    template_name = 'fbv/register.html'
    success_url = reverse_lazy('home')

    def test_func(self):
        return not self.request.user.is_authenticated


def login_fbv(request: HttpRequest) -> HttpResponse:
    form = AuthenticationForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        # username = request.POST.get('username')
        # password = request.POST.get('password')
        # user = authenticate(request, username=username, password=password)
        #
        # if user is not None:
        login(request, form.get_user())
        return redirect('home')

    messages.error(request, "Invalid username or password")

    return render(request, 'fbv/login.html', {"form": form})


@user_passes_test(lambda user: not user.is_authenticated, login_url="home")
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


@login_required
@permission_required('auth.can_set_unusable_password_permission')
def set_unusable_password_view(request):
    form = SetUnusablePasswordForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        selected_user = form.cleaned_data["user"]
        selected_user.set_unusable_password()
        selected_user.save(update_fields=["password"])
        messages.success(request, f"Successfully banned {selected_user.get_username()}")
        return redirect('home')

    return render(request, "accounts/set_unusable_password.html", {"form": form})