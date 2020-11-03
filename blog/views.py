from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Category, Comment, Subscribe
from django.views.generic import ListView, DetailView, CreateView
from .forms import NewCommentForm, SubscribeForm
from django.urls import reverse

# Create your views here.
class HomeView(ListView):
    model = Post
    template_name = 'blog/index.html'
    ordering = ['-date_created']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['subscribeform'] = SubscribeForm()
        return context

class ArticleDetailView(DetailView):
    model = Post
    template_name = 'blog/detail_post.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comment'] = Comment.objects.all()
        context['form'] = NewCommentForm()
        context['subscribeform'] = SubscribeForm()
        return context

class SubscribeCreateView(CreateView):
    model = Subscribe
    form_class = SubscribeForm
    template_name = 'blog/side_widget.html'
    success_url = '/'

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
        return render(request, self.template_name,{'form':form})

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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['subscribeform'] = SubscribeForm()
        return context

    def get_queryset(self):
        content = {
            'cat': self.kwargs['category'].replace('-', ' '),
            'posts': Post.objects.filter(category__name=self.kwargs['category'].replace('-', ' ')),
        }
        return content

def category_list(request):
    category_list = Category.objects.all()
    context = {
        'category_list': category_list,
    }
    return context

def latest_posts(request):
    latest = Post.objects.all()
    context = {
        'latest': latest,
    }
    return context


 