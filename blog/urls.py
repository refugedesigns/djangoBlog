from django.urls import path
from .views import HomeView, ArticleDetailView,CatListView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('post_detail/<str:pk>/', ArticleDetailView.as_view(), name='post_detail'),
    path('category/<category>/', CatListView.as_view(), name='category'),
]