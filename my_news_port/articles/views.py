from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView,DetailView
from .models import Post


class NewsList(ListView):
    model = Post
    ordering = 'title'
    template_name = 'news.html'
    context_object_name = 'news'


class NewsDetail(DetailView):
    model = Post
    template_name = 'news_post.html'
    context_object_name = 'news_post'