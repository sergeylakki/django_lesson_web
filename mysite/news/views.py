from django.shortcuts import render
from django.http import HttpResponse
from .models import Category, News

def index(request):
    #print(request)
    news = News.objects.order_by('-created_at')
    return render(request, 'news/index.html', {'news': news})


def test(request):
    news = News.objects.order_by('-created_at')
    title = "Новости"
    categories = Category.objects.all()
    return render(request, 'news/index2.html', {'news': news, 
    "title": title,
    })


def get_category(request, category_id):
    news = News.objects.filter(category_id=category_id)
    categories = Category.objects.all()
    category = Category.objects.get(pk=category_id)
    return render(request,'news/category.html',{
        "news": news, 
        "category": category,
    })

