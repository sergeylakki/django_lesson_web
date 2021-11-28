from django.db.models.base import Model
from django.db.models import F
from django.forms import forms
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Category, News
from .forms import NewsForm
from django.views.generic import ListView, DetailView, CreateView
from django.urls import reverse_lazy



class HomeNews(ListView):
    model = News
    template_name = "news/news_list.html"#не обязательно
    contex_object_name = "object_list"#Не обязательно имя переменной
    extra_content = {'title': "Главная"}#Только для статичных данных


    #Перекдача доп аргументов в шаблон
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Главная страница'
        return context


    #Изменения дефолта выборки новостей
    def get_queryset(self):
        return News.objects.filter(is_published=True)



class NewsByCategory(ListView):
    model = News
    allow_empty = False#делает 404 при пустом списке

    #Изменения дефолта выборки новостей
    def get_queryset(self):
        return News.objects.filter(category_id=self.kwargs['category_id'], is_published=True)


       #Передача доп аргументов в шаблон
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = Category.objects.get(pk=self.kwargs["category_id"])
        return context


class ViewNews(DetailView):
    model = News
    context_object_name = "news_item"#по умолчанию object
    #pk_url_kwarg = "news_id"
    #Получение обратной связи
    #модель.связная модель_set.all()


        #Изменения дефолта выборки новостей
    def get_object(self):
        #news = get_object_or_404(News, pk=self.kwargs['pk'])
        news = News.objects.get(pk=self.kwargs['pk'])
        news.views += 1
        news.save()
        return news



class CreateNews(CreateView):
    form_class = NewsForm
    template_name = "news/add_news.html"
    #succsess_url = reverse_lazy("home")





















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
            #news = News.objects.create(**form.cleaned_data)
            news = form.save()
            return redirect(news)
    else:
        form = NewsForm()
    return render(request,'news/add_news.html',{"form": form})