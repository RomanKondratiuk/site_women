from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect
from django.urls import reverse
from django.template.loader import render_to_string
from django.template.defaultfilters import slugify

menu = ["About his site", "Add article", "Feedback", "Sign in"]


class MyClass:
    def __init__(self, a, b):
        self.a = a
        self.b = b


def page_not_found(request, exception):
    """ function for not found pages """
    return HttpResponseNotFound("<h1> Page Not Found !!! </h1>")


def index(request):
    data = {
        'title': 'main page',
        'menu': menu,
        'float': 34.33,
        'list': [1, 3, 4, 'abc', False],
        'set': {1, 4, 3, 2, 4},
        'dict': {'key_1': 'value_1', 'key_2': 'value_2'},
        'obj': MyClass(10, 20),
        'url': slugify("Hi python, you are best"), # применение функции "slugify"
    }
    # template = render_to_string('women/index.html')   # 1й вариант
    # return HttpResponse(template)                     # 1й вариант
    return render(request, 'women/index.html', context=data)  # 2й вариант


def about(request):
    data = {'title': 'About this site'}
    return render(request, 'women/about.html', data)


def categories(request, category_id):
    return HttpResponse(f'<h1>Articles by category</h1><p>id: {category_id}</p>')


def categories_by_slug(request, category_slug):
    if request.GET:
        print(request.GET)
    return HttpResponse(f'<h1>Articles by category</h1><p>slug: {category_slug}</p>')


def archive(request, year):
    if year > 2023:
        url = reverse('category_slug', args=('music',))
        return redirect(url)  # return to home page
    return HttpResponse(f'<h1>Archive by years</h1><p>{year}</p>')
