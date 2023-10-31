from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return HttpResponse("This is page for women")


def categories(request, category_id):
    return HttpResponse(f'<h1>Articles by category</h1><p>id: {category_id}</p>')


def categories_by_slug(request, category_slug):
    return HttpResponse(f'<h1>Articles by category</h1><p>id: {category_slug}</p>')


def archive(request, year):
    return HttpResponse(f'<h1>Archive by years</h1><p>{year}</p>')
