from django.shortcuts import render
from .models import Post, Category
from django.views.generic import ListView, DetailView

# Create your views here.
class HomeView(ListView):
    model = Post
    template_name = 'blog/index.html'
    ordering = ['-date_created']

class ArticleDetailView(DetailView):
    model = Post
    template_name = 'blog/detail_post.html'


class CatListView(ListView):
    template_name = 'blog/category.html'
    context_object_name = 'catlist'


    def get_queryset(self):
        content = {
            'cat': self.kwargs['category'],
            'posts': Post.objects.filter(category__name=self.kwargs['category']),
        }
        return content

def category_list(reguest):
    category_list = Category.objects.all()
    context = {
        'category_list': category_list,
    }
    return context

