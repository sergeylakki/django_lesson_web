from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    #path('', views.test,name="home"),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('send_mail/', views.send_mail, name='send_mail'),
    path('', views.HomeNews.as_view(), name='home'),
    path('category/<int:category_id>/', views.NewsByCategory.as_view(), name="category"),
    path('news/<int:pk>/', views.ViewNews.as_view(), name="view_news"),
    path('news/add_news', views.CreateNews.as_view(), name="add_news"),
    #path('category/<int:category_id>/', views.ViewNews.as_view(), name="category"),
    #path('category/<int:category_id>/', views.get_category, name="category"),
    #path('news/<int:news_id>/', views.view_news, name="view_news"),
    path('test/', views.test),
    #path('news/add_news', views.add_news, name="add_news"),
]