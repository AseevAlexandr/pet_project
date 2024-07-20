from django.http import HttpResponse
from django.shortcuts import render


def index(requests):
    return HttpResponse('страница приложения women.')


def categories(requests):
    return HttpResponse('<h1>Статьи по категориям</h1>')
