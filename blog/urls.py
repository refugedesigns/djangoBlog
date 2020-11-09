from django.urls import path
from .views import HomeView, ArticleDetailView,CatListView,CommentCreatView, SubscribeCreateView,postSearchView 

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('post_search/', postSearchView, name='post_search'),
    path('post_detail/<slug:slug>/', ArticleDetailView.as_view(), name='post_detail'),
    path('add_comment/<slug:slug>/', CommentCreatView.as_view(), name='add_comment'),
    path('category/<category>/', CatListView.as_view(), name='category'),
    path('blog/subscribe/', SubscribeCreateView.as_view(), name='subscribe'),
]