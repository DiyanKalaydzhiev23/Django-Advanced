from django.urls import reverse_lazy
from django.views.generic import CreateView
from forumApp.forms import CustomUserForm


class UserRegisterView(CreateView):
    form_class = CustomUserForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('index')
