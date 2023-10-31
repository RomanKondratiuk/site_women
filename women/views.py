from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return HttpResponse("This is page for women")


def categories(request):
    return HttpResponse('<h1>"Articles by category"</h1>')
