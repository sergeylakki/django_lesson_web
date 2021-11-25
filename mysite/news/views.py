from django.shortcuts import render
from django.http import HttpResponse
from .models import News

def index(request):
    #print(request)
    news = News.objects.order_by('-created_at')
    return render(request, 'news/index.html', {'news': news})


def test(request):
    news = News.objects.order_by('-created_at')
    return render(request, 'news/index2.html', {'news': news})
# Create your views here.
