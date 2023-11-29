from django.urls import path
from . import views

urlpatterns = [
    path('', views.posts, name='posts'),
    path('posts/<int:posts_id>/', views.detail_posts, name='detail_posts'),
]