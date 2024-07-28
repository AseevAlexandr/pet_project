from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect, get_object_or_404

from .forms import *
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
               'title': 'Главная страница',
               'cat_selected': 0,
               }
    return render(requests, 'women/index.html', context=context)


def about(requests):
    return render(requests, 'women/about.html', {'menu': menu, 'title': 'О сайте'})


def addpage(requests):
    if requests.method == 'POST':
        form = AddPostForm(requests.POST)
        if form.is_valid():
            # print(form.cleaned_data)
            try:
                Women.objects.create(**form.cleaned_data)
                return redirect('home')
            except:
                form.add_error(None, 'Ошибка добавления')
    else:
        form = AddPostForm()
    return render(requests, 'women/addpage.html', {'form': form, 'menu': menu, 'title': 'Добавление статьи'})


def contact(requests):
    return HttpResponse('Обратная связь')


def login(requests):
    return HttpResponse('Авторизация')


def pageNotFound(requests, exception):
    return HttpResponseNotFound("<h1>Страница не найдена</h1>")


def show_post(requests, post_slug):
    post = get_object_or_404(Women, slug=post_slug)

    context = {
        'post': post,
        'menu': menu,
        'title': post.title,
        'cat_selected': post.cat_id,
    }


    return render(requests, 'women/post.html', context=context)


def show_category(requests, cat_id):
    posts = Women.objects.filter(cat_id=cat_id)


    if len(posts) == 0:
        raise Http404()


    context = {'posts': posts,
               'menu': menu,
               'title': 'Отображение по рубрикам',
               'cat_selected': 0,
               }
    return render(requests, 'women/index.html', context=context)

