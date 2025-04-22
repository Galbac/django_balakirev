from django.http import HttpResponse, Http404, HttpResponsePermanentRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from women.models import Women, Category

menu = [{'title': "О сайте", 'url_name': 'about'},
        {'title': "Добавить статью", 'url_name': 'addpage'},
        {'title': "Обратная связь", 'url_name': 'contact'},
        {'title': "Войти", 'url_name': 'login'}
        ]


# Функция, которая проверяет, является ли число простым


def index(request):
    posts = Women.published.all()
    data = {
        'title': 'Главная страница',
        'menu': menu,
        'posts': posts
    }
    return render(request, 'women/index.html', data)


def about(request):
    return render(request, 'women/about.html', {"title": "О сайте", "menu": menu})


def show_post(request, post_slug):
    post = get_object_or_404(Women, slug=post_slug)
    data = {
        'title': post.title,
        'menu': menu,
        'post': post,
        "cat_selected": 1
    }
    return render(request, 'women/post.html', context=data)


def addpage(request):
    return HttpResponse("Добавление статьи")


def contact(request):
    return HttpResponse("Обратная связь")


def show_category(request, cat_slug):
    category = get_object_or_404(Category, slug=cat_slug)
    posts = Women.published.filter(cat_id=category.pk)
    data = {
        'title': f'Рубрика: {category.name}',
        'menu': menu,
        'posts': posts,
        "cat_selected": category.pk
    }
    return render(request, 'women/index.html', data)


def login(request):
    return HttpResponse("Авторизация")
