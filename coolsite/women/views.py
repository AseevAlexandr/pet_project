from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect


def index(requests):
    return HttpResponse('страница приложения women.')


def categories(requests, catid):
    if(requests.GET):
        print(requests.GET)
    return HttpResponse(f'<h1>Статьи по категориям</h1><p>{catid}</p>')


def archive(requests, year):
    if int(year) > 2020:
        return redirect('home', permanent= True)

    return HttpResponse(f"<h1>Архив по годам</h1><p>{year}</p>")


def pageNotFound(requests, exception):
    return HttpResponseNotFound("<h1>Страница не найдена</h1>")