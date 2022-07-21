from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post
from .filters import NewsFilter
from .forms import PostForm


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


class PostCreate(CreateView):
    form_class = PostForm
    model = Post
    template_name = 'create.html'

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

# def post_create(request):
#     if request.method == 'POST':
#         form = PostForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect ('/news/')
#
#     form = PostForm()
#     return render(request, 'create.html', {'form': form})


