from django.shortcuts import render
from .models import Post, Category
from django.views.generic import ListView, DetailView

# Create your views here.
class HomeView(ListView):
    model = Post
    template_name = 'blog/index.html'
    ordering = ['-date_created']

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(HomeView, self).get_context_data(*args, **kwargs)
        context["cat_menu"] = cat_menu
        return context

class ArticleDetailView(DetailView):
    model = Post
    template_name = 'blog/detail_post.html'

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(ArticleDetailView, self).get_context_data(*args, **kwargs)
        context["cat_menu"] = cat_menu
        return context

def CategoryView(request, cats):
    category_posts = Post.objects.filter(category=cats)
    cat_menu = Category.objects.all()
    return render(request, 'blog/category.html', {'cats':cats,'category_posts':category_posts, 'cat_menu': cat_menu})
