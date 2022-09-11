from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView, View
from .models import Post, Author, Subscribers
from .filters import NewsFilter
from .forms import PostForm
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.shortcuts import render, reverse, redirect
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.http import HttpResponse
from django.views import View
from .tasks import send_email_add_news, send_email_week
from django.core.cache import cache

import logging
logger = logging.getLogger(__name__)

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

    def get_object(self, *args, **kwargs):  # переопределяем метод получения объекта, как ни странно
        obj = cache.get(f'post-{self.kwargs["pk"]}', None)  # кэш очень похож на словарь, и метод get действует так же. Он забирает значение по ключу, если его нет, то забирает None.
        # если объекта нет в кэше, то получаем его и записываем в кэш
        if not obj:
            obj = super().get_object(queryset=self.queryset)
            cache.set(f'post-{self.kwargs["pk"]}', obj)
        return obj

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


class SubscribersView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'category_subscribers.html', {})

    def post(self, request, *args, **kwargs):
        subscribers = Subscribers(
            user=request.POST['user'],
            message=request.POST['category'],
        )
        subscribers.save()

        # получаем наш html
        html_content = render_to_string(
            'subscribers_created.html',
            {
                'subscribers': subscribers,
            }
        )

        # в конструкторе уже знакомые нам параметры, да? Называются правда немного по другому, но суть та же.
        msg = EmailMultiAlternatives(
            subject=f'{subscribers.user}',
            body=subscribers.category,
            from_email='***@yandex.ru',
            to=['efremova.alevtina@gmail.com'],  # это то же, что и recipients_list
        )
        msg.attach_alternative(html_content, "text/html")  # добавляем html

        msg.send()  # отсылаем

        return redirect('subscribers:category_subscribers')

class IndexView(View):
    def get(self, request):
        send_email_week.delay()
        send_email_add_news.delay()
        return HttpResponse('message')
