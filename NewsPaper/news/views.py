from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView
from .models import Post, Author
from .filters import NewsFilter
from .forms import *
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin


class NewsList(ListView):
    model = Post
    data = '-data_create_post'
    template_name = 'news.html'
    context_object_name = 'news'
    paginate_by = 10

class SearchList(ListView):
    model = Post
    template_name = 'search.html'
    context_object_name = 'news'

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = NewsFilter(self.request.GET, queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filterset'] = self.filterset
        return context

class NewsDetail(DetailView):
    model = Post
    template_name = 'post.html'
    context_object_name = 'post'


class PostCreate(PermissionRequiredMixin, CreateView):
    form_class = PostForm
    model = Post
    template_name = 'create.html'
    permission_required = ('news.add_post', 'news.change_post')


    def form_valid(self, form):
        post = form.save(commit=False)
        post.vid = 'Статья'
        return super().form_valid(form)

class PostUpdateView(UpdateView):
    model = Post
    template_name = 'edit.html'
    fields = ['author', 'vid', 'title_post', 'text_post', 'category']


class PostDeleteView(DeleteView):
    model = Post
    template_name = 'delete.html'
    success_url = reverse_lazy('home')

class AuthorList(ListView):
    model = Post
    template_name = 'authory.html'
    context_object_name = 'author'
    paginate_by = 10


class AuthorProtectedView(LoginRequiredMixin, TemplateView):
    model = Author
    template_name = 'author_edit.html'
    fields = ['author_user']

