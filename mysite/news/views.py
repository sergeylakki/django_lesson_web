from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Category, News
from .forms import NewsForm


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

def view_news(request,news_id):
    news_item = get_object_or_404(News, pk=news_id)
    #news_item = News.objects.get(pk=news_id)
    return render(request, 'news/view_news.html',{"news_item":news_item})

def add_news(request):
    if request.method == "POST":
        form = NewsForm(request.POST)
        if form.is_valid():
            news = News.objects.create(**form.cleaned_data)
            return redirect(news)
    else:
        form = NewsForm()
    return render(request,'news/add_news.html',{"form": form})