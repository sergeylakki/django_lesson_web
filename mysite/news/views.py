from django.db.models.base import Model
from django.db.models import F
from django.db.models.query import QuerySet
from django.forms import forms
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Category, News
from .forms import NewsForm, UserRegisterForm,UserLoginForm
from django.views.generic import ListView, DetailView, CreateView
from django.urls import reverse_lazy
from .utils import MymMxin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator
from django.contrib import messages
from django.contrib.auth import authenticate, get_user, login,logout

def register(request):
    if request.method =='POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            print(form)
            form.save()
            messages.success(request,'Вы успешно зарегестрировались  ')
            return redirect('login')
        else:
            messages.error(request,'Ошибка регистрации  ')
    else:    
        form = UserRegisterForm()
    return render(request, "news/register.html",{"form":form})

def user_logout(request):
    logout(request)
    return redirect('home')


def user_login(request):
    if request.method == 'POST':
        print("Hello")
        form = UserLoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
            
        else:
            messages.error(request,'Ошибка входа ')
    else:   
        form = UserLoginForm() 
    return render(request, "news/login.html",{"form":form})


class HomeNews(MymMxin,ListView):
    model = News
    template_name = "news/news_list.html"#не обязательно
    contex_object_name = "object_list"#Не обязательно имя переменной
    extra_content = {'title': "Главная"}#Только для статичных данных
    queryset = News.objects.filter(is_published=True).select_related("category")
    mixin_prop = 'hello world '
    paginate_by = 2

    #Перекдача доп аргументов в шаблон
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Главная страница'
        return context


    #Изменения дефолта выборки новостей
   # def get_queryset(self):
   #     return News.objects.filter(is_published=True).select_related("category")



class NewsByCategory(ListView):
    model = News
    allow_empty = False#делает 404 при пустом списке
    paginate_by = 2
    #Изменения дефолта выборки новостей
    def get_queryset(self):
        return News.objects.filter(category_id=self.kwargs['category_id'], is_published=True).select_related("category")


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



class CreateNews(LoginRequiredMixin, CreateView):
    form_class = NewsForm
    template_name = "news/add_news.html"
    #succsess_url = reverse_lazy("home")
    login_url = '/'




















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