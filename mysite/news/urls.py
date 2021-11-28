from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.test,name="home"),
    path('category/<int:category_id>/', views.get_category, name="category"),
    path('news/<int:news_id>/', views.view_news, name="view_news"),
    path('test/', views.test),
    path('news/add_news', views.add_news, name="add_news"),
]