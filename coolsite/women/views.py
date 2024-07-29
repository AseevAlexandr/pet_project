from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DeleteView, CreateView

from .forms import *
from .models import  *


menu = [
    {'title': "О сайте", 'url_name': 'about'},
    {'title': "Добавить статью", 'url_name': 'addpage'},
    {'title': "Обратная связь", 'url_name': 'contact'},
    {'title': "Войти", 'url_name': 'login'}
]


class WomenHome(ListView):
    model = Women
    template_name = 'women/index.html'
    context_object_name = 'posts'


    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        context['title'] = 'Главная страница'
        context['cat_selected'] = 0
        return context


    def get_queryset(self):
        return Women.objects.filter(is_published = True)



# def index(requests):
#     posts = Women.objects.all()
#
#     context = {'posts': posts,
#                'menu': menu,
#                'title': 'Главная страница',
#                'cat_selected': 0,
#                }
#     return render(requests, 'women/index.html', context=context)


def about(requests):
    return render(requests, 'women/about.html', {'menu': menu, 'title': 'О сайте'})


# def addpage(requests):
#     if requests.method == 'POST':
#         form = AddPostForm(requests.POST, requests.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect('home')
#     else:
#         form = AddPostForm()
#     return render(requests, 'women/addpage.html', {'form': form, 'menu': menu, 'title': 'Добавление статьи'})
class AddPage(CreateView):
    form_class = AddPostForm
    template_name = 'women/addpage.html'


    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        context['title'] = 'Добавление ствтьи'
        return context


def contact(requests):
    return HttpResponse('Обратная связь')


def login(requests):
    return HttpResponse('Авторизация')


def pageNotFound(requests, exception):
    return HttpResponseNotFound("<h1>Страница не найдена</h1>")


# def show_post(requests, post_slug):
#     post = get_object_or_404(Women, slug=post_slug)
#
#     context = {
#         'post': post,
#         'menu': menu,
#         'title': post.title,
#         'cat_selected': post.cat_id,
#     }
#
#
#     return render(requests, 'women/post.html', context=context)
class ShowPost(DeleteView):
    model = Women
    template_name = 'women/post.html'
    slug_url_kwarg = 'post_slug'
    context_object_name = 'post'


    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        context['title'] = context['post']
        return context


class WomenCategory(ListView):
    model = Women
    template_name = 'women/index.html'
    context_object_name = 'posts'
    allow_empty = False


    def get_queryset(self):
        return Women.objects.filter(cat__slug=self.kwargs['cat_slug'], is_published= True)


    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        context['title'] = 'Категория - ' + str(context['posts'][0].cat)
        context['cat_selected'] = context['posts'][0].cat_id
        return context
# def show_category(requests, cat_id):
#     posts = Women.objects.filter(cat_id=cat_id)
#
#
#     if len(posts) == 0:
#         raise Http404()
#
#
#     context = {'posts': posts,
#                'menu': menu,
#                'title': 'Отображение по рубрикам',
#                'cat_selected': 0,
#                }
#     return render(requests, 'women/index.html', context=context)

