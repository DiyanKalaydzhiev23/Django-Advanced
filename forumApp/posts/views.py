from datetime import datetime

from django.contrib.auth.decorators import permission_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.db import connection
from django.db.models import Q
from django.forms import modelform_factory
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.template.context_processors import request
from django.urls import reverse, reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView, RedirectView, CreateView, UpdateView, DeleteView, FormView, DetailView, \
    ListView
from django.views.generic.edit import FormMixin

from posts.decorators import measure_execution_time
from posts.forms import PostCreateForm, PostDeleteForm, SearchForm, CommentFormSet
from posts.mixins import TimeRestrictedMixin
from posts.models import Post


class IndexView(TemplateView):
    # template_name = 'index.html'  # static way
    # extra_context = {  # static way
    #     "current_time": datetime.now(),
    # }

    def get_context_data(self, **kwargs):
        super().get_context_data(**kwargs)
        kwargs.update({  # static way
            "current_time": datetime.now(),
        })
        return kwargs

    def get_template_names(self):  # dynamic way
        if self.request.user.is_superuser:
            return ['index_for_admin.html']

        return ['jhfqwkandoixeu', 'index.html']


def approve_post(request, pk):
    if request.method == "POST":
        post = Post.objects.get(pk=pk)
        post.approved = True
        post.save()

        return redirect('dashboard')


@method_decorator(name='dispatch', decorator=measure_execution_time)
class Dashboard(ListView, PermissionRequiredMixin):
    model = Post
    template_name = "posts/dashboard.html"
    paginate_by = 4
    query_param = "query"
    form_class = SearchForm
    permission_required = 'posts.approve_post'

    def get_context_data(self, *, object_list=None, **kwargs):
        kwargs.update({
            "search_form": self.form_class(),
            "query": self.request.GET.get(self.query_param, ''),
        })
        return super().get_context_data(object_list=object_list, **kwargs)

    def get_queryset(self):
        queryset = self.model.objects.all()
        search_value = self.request.GET.get(self.query_param)

        if not self.has_permission():
            queryset = queryset.filter(approved=True)

        if search_value:
            queryset = queryset.filter(
                Q(title__icontains=search_value)
                    |
                Q(content__icontains=search_value)
                    |
                Q(author__icontains=search_value)
            )

        return queryset

class CreatePost(LoginRequiredMixin, TimeRestrictedMixin, CreateView):
    model = Post
    form_class = PostCreateForm
    success_url = reverse_lazy('dashboard')
    template_name = 'posts/add-post.html'


class EditPost(TimeRestrictedMixin, UpdateView):
    model = Post
    success_url = reverse_lazy('dashboard')
    template_name = 'posts/edit-post.html'

    def get_form_class(self):
        if self.request.user.is_superuser:
            return modelform_factory(Post, fields='__all__')
        else:
            return modelform_factory(Post, fields=('content',),)


class PostDetails(DetailView, FormMixin):
    model = Post
    template_name = "posts/post-details.html"  # Not needed if named as Django expects
    form_class = CommentFormSet

    def get_context_data(self, **kwargs):
        kwargs.update({
            "formset": self.get_form_class()(),
        })
        return super().get_context_data(**kwargs)

    def get_success_url(self):
        return reverse_lazy('post-details', kwargs={'pk': self.kwargs.get(self.pk_url_kwarg)})

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        comment_form_set = self.get_form_class()(request.POST)

        if comment_form_set.is_valid():
            for form in comment_form_set:
                comment = form.save(commit=False)
                comment.author = request.user.username
                comment.post = self.object
                comment.save()

            return self.form_valid(comment_form_set)


def post_details(request, pk: int):
    post = Post.objects.get(pk=pk)

    context = {
        "post": post,
        # "formset": comment_form_set,
    }

    return render(request, 'posts/post-details.html', context)


class DeletePost(DeleteView, FormView):
    model = Post
    form_class = PostDeleteForm
    template_name = 'posts/delete-post.html'
    success_url = reverse_lazy('dashboard')

    def get_initial(self):
        pk = self.kwargs.get(self.pk_url_kwarg)
        post = self.model.objects.get(pk=pk)
        return post.__dict__

class MyRedirectView(RedirectView):
    # url = 'http://localhost:8000/dashboard/'
    # pattern_name = 'dashboard'
    # Both static ways

    def get_redirect_url(self, *args, **kwargs):  # dynamic way
        return reverse('dashboard') + "?query=Django"


def unsafe_view(request):
    user_input = request.GET.get('username')
    query = f"SELECT * FROM auth_user WHERE username = '{user_input}'"

    with connection.cursor() as cursor:
        cursor.execute(query)
        rows = cursor.fetchall()

    return JsonResponse(data={"data": rows})

