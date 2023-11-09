from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect
from django.urls import reverse
from django.template.loader import render_to_string
from django.template.defaultfilters import slugify

menu = [{'title': "About his site", 'url_name': 'about'},
        {'title': "Add page", 'url_name': 'addpage'},
        {'title': "Feedback", 'url_name': 'contact'},
        {'title': "Login", 'url_name': 'login'},
        ]

# data_db = [
#     {'id': 1, 'category': 'car', 'title': 'bmw', 'year': 2022, 'in_stock': True},
#     {'id': 2, 'category': 'moto', 'title': 'yamaha', 'year': 2020, 'in_stock': False},
#     {'id': 3, 'category': 'boat', 'title': 'honda', 'year': 2010, 'in_stock': True}
# ]
data_db = [
    {'id': 1, 'title': 'Анджелина Джоли', 'content': '''
      <h1>Анджелина Джоли</h1>
    (англ. Angelina Jolie[7], при рождении Войт (англ. Voight), ранее Джоли Питт (англ. Jolie Pitt); род. 4 июня 1975, Лос-Анджелес, Калифорния, США) — американская актриса кино, телевидения и озвучивания, кинорежиссёр, сценаристка, продюсер, фотомодель, посол доброй воли ООН.
    Обладательница премии «Оскар», трёх премий «Золотой глобус» (первая актриса в истории, три года подряд выигравшая премию) и двух «Премий Гильдии киноактёров США».''',
     'is_published': True},
    # {'id': 1, 'title': 'Анджелина Джоли', 'content': 'Биография Джулия Робертс', 'is_published': True},
    {'id': 2, 'title': 'Марго Робби', 'content': 'Биография Марго Робби', 'is_published': False},
    {'id': 3, 'title': 'Джулия Робертс', 'content': 'Биография Джулия Робертс', 'is_published': True},
]


class MyClass:
    def __init__(self, a, b):
        self.a = a
        self.b = b


def page_not_found(request, exception):
    """ function for not found pages """
    return HttpResponseNotFound("<h1> Page Not Found !!! </h1>")


def index(request):
    data = {
        'menu': menu,
        'title': 'Main Page',
        'posts': data_db,
    }
    # template = render_to_string('women/index.html')   # 1й вариант
    # return HttpResponse(template)                     # 1й вариант
    return render(request, 'women/index.html', context=data)  # 2й вариант


def about(request):
    data = {'title': 'About this site'}
    return render(request, 'women/about.html', {'title': 'About this site', 'menu': menu})


def show_post(request, post_id):
    return HttpResponse(f"View article with ID:{post_id}")


def addpage(request):
    return HttpResponse("Add page")


def contact(request):
    return HttpResponse("Feedback")


def login(request):
    return HttpResponse("Log in")
