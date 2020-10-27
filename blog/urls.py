from django.urls import path
from .views import HomeView, ArticleDetailView,CategoryView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('post_detail/<str:pk>/', ArticleDetailView.as_view(), name='post_detail'),
    path('category/<str:cats>/', CategoryView, name='category'),
]