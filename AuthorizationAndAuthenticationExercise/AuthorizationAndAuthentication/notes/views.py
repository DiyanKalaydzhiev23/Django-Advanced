from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.db.models import QuerySet
from django.views.generic import ListView, DetailView

from notes.models import Note


class NoteListView(LoginRequiredMixin, ListView):
    def get_queryset(self) -> QuerySet[Note]:
        qs = Note.objects.select_related('owner')

        if not self.request.user.has_perm('notes.can_access_all_notes'):
            return qs.filter(owner=self.request.user)

        return qs


class NoteDetailView(UserPassesTestMixin, LoginRequiredMixin, DetailView):
    queryset = Note.objects.select_related('owner')

    def test_func(self) -> bool:
        return (
                self.request.user.has_perm('notes.can_access_all_notes')
                    or
                self.get_object().owner == self.request.user
        )