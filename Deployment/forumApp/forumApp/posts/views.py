import asyncio
from datetime import datetime, time
from time import sleep

from asgiref.sync import sync_to_async
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.mail import send_mail
from django.forms import modelform_factory
from django.http import HttpResponseNotAllowed, HttpResponse
from django.shortcuts import render, redirect
from django.template.context_processors import request
from django.urls import reverse_lazy
from django.utils.decorators import classonlymethod, method_decorator
from django.views.generic import TemplateView, RedirectView, ListView, FormView, CreateView, UpdateView, DeleteView, \
    DetailView
from forumApp.decorators import measure_execution_time
from forumApp.posts.forms import PostCreateForm, PostDeleteForm, SearchForm, PostEditForm, CommentFormSet
from forumApp.posts.mixins import TimeRestrictedMixin
from forumApp.posts.models import Post

UserModel = get_user_model()

class BaseView:
    @classonlymethod
    def as_view(cls):

        def view(request, *args, **kwargs):
            view_instance = cls()
            return view_instance.dispatch(request, *args, **kwargs)

        return view

    def dispatch(self, request, *args, **kwargs):
        if request.method == "GET":
            return self.get(request, *args, **kwargs)
        elif request.method == "POST":
            return self.post(request, *args, **kwargs)



@method_decorator(measure_execution_time, name='dispatch')
class IndexView(TimeRestrictedMixin, TemplateView):
    template_name = 'common/index.html'  # static way
    end_time = time(21, 43)
    extra_context = {
        'static_time': datetime.now(),
    }  # static way

    def get_context_data(self, **kwargs):  # dynamic way
        context = super().get_context_data(**kwargs)

        context['dynamic_time'] = datetime.now()

        return context

    def get_template_names(self):  # dynamic way
        if self.request.user.is_authenticated:
            return ['common/index_logged_in.html']
        else:
            return ['common/index.html']

class DashboardView(ListView, FormView):
    template_name = 'posts/dashboard.html'
    context_object_name = 'posts'
    form_class = SearchForm
    paginate_by = 2
    success_url = reverse_lazy('dash')
    model = Post

    def get_queryset(self):
        queryset = self.model.objects.all()

        if 'posts.can_approve_posts' not in self.request.user.get_group_permissions() or not self.request.user.has_perm('posts.can_approve_posts'):
            queryset = queryset.filter(approved=True)

        if 'query' in self.request.GET:
            query = self.request.GET.get('query')
            queryset = queryset.filter(title__icontains=query)

        return queryset


async def fetch_post_and_users(post_id):
    post = await Post.objects.select_related('author').aget(pk=post_id)
    all_users = await sync_to_async(UserModel.objects.exclude)(id=post.author.id)
    all_user_to_list = await sync_to_async(list)(all_users)
    return post, all_user_to_list


async def send_slow_email(subject, message, origin, to):
    await asyncio.sleep(5)
    await sync_to_async(send_mail)(
        subject=subject,
        message=message,
        from_email=origin,
        recipient_list=[to]
    )


async def notify_all_users(request, post_id):
    post, all_users = await fetch_post_and_users(post_id)

    subject = f"New Post: {post.title}"
    message = f"{post.author.username} wrote:\n\n{post.content}"

    email_tasks = [
        send_slow_email(
            subject,
            message,
            'no-reply@forumapp.com',
            user.email,
        )  # Does not call the func it returns an object
        for user in all_users
    ]

    await asyncio.gather(*email_tasks)

    return HttpResponse("Done")


def approve_post(request, pk):
    post = Post.objects.get(pk=pk)
    post.approved = True
    post.save()

    return redirect(
        request.META.get('HTTP_REFERER')
    )


class AddPostView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostCreateForm
    template_name = 'posts/add-post.html'
    success_url = reverse_lazy('dash')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class EditPostView(UpdateView):
    model = Post
    template_name = 'posts/edit-post.html'
    success_url = reverse_lazy('dash')

    def get_form_class(self):
        if self.request.user.is_superuser:
            return modelform_factory(Post, fields=('title', 'content', 'author', 'languages'))
        else:
            return modelform_factory(Post, fields=('content',))



class PostDetailView(DetailView):
    model = Post
    template_name = 'posts/details-post.html'

    def get_context_data(self, **kwargs):
        print(PostDetailView.__mro__)
        context = super().get_context_data(**kwargs)
        context['formset'] = CommentFormSet()
        return context

    def post(self, request, *args, **kwargs):
        post = self.get_object()
        formset = CommentFormSet(request.POST)

        if formset.is_valid():
            for form in formset:
                if form.cleaned_data:
                    comment = form.save(commit=False)
                    comment.post = post
                    comment.save()

            return redirect('details-post', pk=post.id)

        context = self.get_context_data()
        context['formset'] = formset

        return self.render_to_response(context)


#
# def details_page(request, pk: int):
#     post = Post.objects.get(pk=pk)
#     formset = CommentFormSet(request.POST or None)
#
#     if request.method == "POST":
#         if formset.is_valid():
#             for form in formset:
#                 if form.cleaned_data:
#                     comment = form.save(commit=False)
#                     comment.post = post
#                     comment.save()
#
#             return redirect('details-post', pk=post.id)
#
#     context = {
#         "post": post,
#         "formset": formset,
#     }
#
#     return render(request, 'posts/details-post.html', context)


class DeletePostView(DeleteView, FormView):
    model = Post
    form_class = PostDeleteForm
    template_name = 'posts/delete-post.html'
    success_url = reverse_lazy('dash')

    def get_initial(self):
        pk = self.kwargs.get(self.pk_url_kwarg)
        post = Post.objects.get(pk=pk)
        return post.__dict__

class RedirectHomeView(RedirectView):
    url = reverse_lazy('index')  # static way

    # def get_redirect_url(self, *args, **kwargs):  # dynamic_way
    #     pass
    #
