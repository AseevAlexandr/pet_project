from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect

from .models import  *


menu = [
    {'title': "О сайте", 'url_name': 'about'},
    {'title': "Добавить статью", 'url_name': 'addpage'},
    {'title': "Обратная связь", 'url_name': 'contact'},
    {'title': "Войти", 'url_name': 'login'}
]

def index(requests):
    posts = Women.objects.all()
    context = {'posts': posts,
               'menu': menu,
               'title': 'Главная страница'
               }
    return render(requests, 'women/index.html', context=context)


def about(requests):
    return render(requests, 'women/about.html', {'menu': menu, 'title': 'О сайте'})


# def index(requests):
#     return HttpResponse('страница приложения women.')


def addpage(requests):
    return HttpResponse('Добавить статью')


def contact(requests):
    return HttpResponse('Обратная связь')


def login(requests):
    return HttpResponse('Авторизация')


def pageNotFound(requests, exception):
    return HttpResponseNotFound("<h1>Страница не найдена</h1>")


def show_post(requests, post_id):
    return HttpResponse(f"Отображение статьи с id = {post_id}")
