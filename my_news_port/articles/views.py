from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from .models import Post,Category #Subscription
from .filters import NewsFilter
from .forms import PostForm
from django.urls import reverse_lazy
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from django.core.cache import cache
from django.views.decorators.csrf import csrf_protect
from django.db.models import Exists, OuterRef

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
    def get_object(self, *args, **kwargs):
        obj = cache.get(f'news - {self.kwargs["pk"]}', None)
        if not obj:
            obj = super().get_object(queryset=self.queryset)
            cache.set(f'product-{self.kwargs["pk"]}', obj)
            return obj

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



class NewsCreate(PermissionRequiredMixin, CreateView):
    permission_required = ('articles.add_post',)
    form_class = PostForm
    model = Post
    template_name = 'news_edit.html'

class NewstUpdate(PermissionRequiredMixin, UpdateView):
    permission_required = ('articles.create_post')
    form_class = PostForm
    model = Post
    template_name = 'news_edit.html'


class NewsDelete(PermissionRequiredMixin, DeleteView):
    permission_required = ('articles.delete_post',)
    model = Post
    template_name = 'news_delete.html'
    success_url = reverse_lazy('news_list')



class CategoryListView(NewsList):
    model = Post
    template_name = 'category_list_sub.html'
    context_object_name = 'category_news_list'

    def get_queryset(self):
        self.postCategory = get_object_or_404(Category,id =self.kwargs['pk'])
        queryset = Post.objects.filter(postCategory = self.postCategory).order_by('-dateTime')
        return queryset


    def get_context_data(self, **kwargs):
        context = super().get_context_data(*kwargs)
        context['is_not_subscriber'] = self.request.user not in self.postCategory.subscribers.all()
        context['category'] = self.postCategory
        return context


@login_required
def subscribe(request, pk):
    user = request.user
    category = Category.objects.get(id=pk)
    category.subscribers.add(user)

    message = 'Вы успешно подписались на рассылку новостей категории'
    return render(request, 'subscriptions.html', {'category':category, 'message':message})



def index(request):
    try:
        posts = Post.objects.all()
        my_file = open('some.txt','a')
        my_file.write('Info {} done!\n'.format(posts))
        my_file.close()

    except:
        my_file = open('some.txt','a')
        my_file.write('Error {} failed\n'.format('new'))
        my_file.close()
    news = Post.objects.all()
    return render(request, 'index.html', context={'news':news})