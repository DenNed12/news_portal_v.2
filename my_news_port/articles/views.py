from django.shortcuts import render, HttpResponseRedirect

# Create your views here.
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from .models import Post
from .filters import NewsFilter
from .forms import PostForm
from django.urls import reverse_lazy



class NewsList(ListView):
    model = Post
    ordering = 'title'
    template_name = 'news.html'
    context_object_name = 'news'
    paginate_by = 3

class NewsDetail(DetailView):
    model = Post
    template_name = 'news_post.html'
    context_object_name = 'news_post'


class NewsSearch(ListView):
    model = Post
    ordering = 'title'
    template_name = 'news_search.html'
    context_object_name = 'news'
    paginate_by = 2

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = NewsFilter(self.request.GET, queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filterset'] = self.filterset
        return context



class NewsCreate(CreateView):
    form_class = PostForm
    model = Post
    template_name = 'news_edit.htm'

class NewstUpdate(UpdateView):
    form_class = PostForm
    model = Post
    template_name = 'news_edit.html'


class NewsDelete(DeleteView):
    model = Post
    template_name = 'news_delete.html'
    success_url = reverse_lazy('news_list')