from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.test,name="home"),
    path('category/<int:category_id>/', views.get_category, name="category"),
    path('test/', views.test)
]