from django.urls import path
from .views import HomeView, ArticleDetailView,CatListView,CommentCreatView 

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('<slug:slug>/', ArticleDetailView.as_view(), name='post_detail'),
    path('<slug:slug>/add_comment/', CommentCreatView.as_view(), name='add_comment'),
    path('category/<category>/', CatListView.as_view(), name='category'),
]