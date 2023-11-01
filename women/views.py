from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render


def page_not_found(request, exception):
    """ function for not found pages """
    return HttpResponseNotFound("<h1> Page Not Found !!! </h1>")


def index(request):
    return HttpResponse("This is page for women")


def categories(request, category_id):
    return HttpResponse(f'<h1>Articles by category</h1><p>id: {category_id}</p>')


def categories_by_slug(request, category_slug):
    if request.GET:
        print(request.GET)
    return HttpResponse(f'<h1>Articles by category</h1><p>id: {category_slug}</p>')


def archive(request, year):
    if year > 2023:
        raise Http404()
    return HttpResponse(f'<h1>Archive by years</h1><p>{year}</p>')
