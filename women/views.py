from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.template.loader import render_to_string
from django.template.defaultfilters import slugify

from women.models import Women, Category, TagPost

menu = [{'title': "About his site", 'url_name': 'about'},
        {'title': "Add page", 'url_name': 'addpage'},
        {'title': "Feedback", 'url_name': 'contact'},
        {'title': "Login", 'url_name': 'login'},
        ]


class MyClass:
    def __init__(self, a, b):
        self.a = a
        self.b = b


def page_not_found(request, exception):
    """ function for not found pages """
    return HttpResponseNotFound("<h1> Page Not Found !!! </h1>")


def index(request):
    posts = Women.published.all().select_related('cat')
    data = {
        'menu': menu,
        'title': 'Отображение по рубрикам',
        'posts': posts,
        'cat_selected': 0,
    }
    # template = render_to_string('women/index.html')   # 1й вариант
    # return HttpResponse(template)                     # 1й вариант
    return render(request, 'women/index.html', context=data)  # 2й вариант


def about(request):
    data = {'title': 'About this site'}
    return render(request, 'women/about.html', {'title': 'About this site', 'menu': menu})


def show_post(request, post_slug):
    post = get_object_or_404(Women, slug=post_slug)

    data = {
        'title': post.title,
        'menu': menu,
        'post': post,
        'cat_selected': 1,
    }
    return render(request, 'women/post.html', data)


def addpage(request):
    return HttpResponse("Add page")


def contact(request):
    return HttpResponse("Feedback")


def login(request):
    return HttpResponse("Log in")


def show_category(request, cat_slug):
    category = get_object_or_404(Category, slug=cat_slug)
    posts = Women.published.filter(cat_id=category.pk).select_related('cat')
    data = {
        'title': f'Рубрика: {category.name}',
        'menu': menu,
        'posts': posts,
        'cat_selected': category.pk,
    }
    return render(request, 'women/index.html', context=data)


def show_tag_postlist(request, tag_slug):
    tag = get_object_or_404(TagPost, slug=tag_slug)
    posts = tag.tags.filter(is_published=Women.Status.PUBLISHED).select_related('cat')

    data = {
        'title': f'Тег: {tag.tag}',
        'menu': menu,
        'posts': posts,
        'cat_selected': None,
    }

    return render(request, 'women/index.html', context=data)
