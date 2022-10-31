from django.shortcuts import render
from django.http import HttpResponse

from .models import News


def index(request):
    news = News.objects.all
    context = {'news':news, 'title':'Список новостей'}
    return render(request, 'news/index.html', context)


# Response создает то, что будет на нашей странице
# Create your views here.
def test(request):
    return HttpResponse('<h1>Тестовая страница</h1')


