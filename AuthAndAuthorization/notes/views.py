from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views.generic import ListView
from notes.models import Note


class HomeView(PermissionRequiredMixin, LoginRequiredMixin, ListView):
    model = Note
    template_name = 'notes/home.html'
    permission_required = 'notes.view_note'