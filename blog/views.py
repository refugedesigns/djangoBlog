from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Category, Comment
from django.views.generic import ListView, DetailView, CreateView
from .forms import NewCommentForm
from django.urls import reverse, reverse_lazy

# Create your views here.
class HomeView(ListView):
    model = Post
    template_name = 'blog/index.html'
    ordering = ['-date_created']

class ArticleDetailView(DetailView):
    model = Post
    template_name = 'blog/detail_post.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comment'] = Comment.objects.all()
        context['form'] = NewCommentForm()
        return context

class CommentCreatView(CreateView):
    model = Comment
    form_class = NewCommentForm

    def form_valid(self, form):
        post = get_object_or_404(Post, slug=self.kwargs ['slug'])
        form.instance.post = post
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('post_detail', kwargs={'slug': self.object.post.slug})


class CatListView(ListView):
    template_name = 'blog/category.html'
    context_object_name = 'catlist'


    def get_queryset(self):
        content = {
            'cat': self.kwargs['category'].replace('-', ' '),
            'posts': Post.objects.filter(category__name=self.kwargs['category'].replace('-', ' ')),
        }
        return content

def category_list(reguest):
    category_list = Category.objects.all()
    context = {
        'category_list': category_list,
    }
    return context


# class ArticleCommentView(CreateView):
#     model = Comment
#     form_class = NewCommentForm
#     template_name = 'blog/comments.html'

#     def get_absolute_url(self):
#         return reverse('post_detail/', args=(str(self.id)))
 