from django.urls import path

from . import views

app_name = 'posts'
urlpatterns = [
    path('', views.index),
    path('group/<slug:slug>/', views.group_posts),
    path('posts/', views.posts, name='posts'),
    ]
