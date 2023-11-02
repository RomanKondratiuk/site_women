from django.urls import path, re_path, register_converter

from . import views
from . import converters

register_converter(converters.FourDigitYearConverter, "year4")


urlpatterns = [
    path('', views.index, name='home'),  # http://127.0.0.1:8000
    path('about/', views.about, name='about'),
    path('category/<int:category_id>/', views.categories, name='category_id'),  # http://127.0.0.1:8000/category/1/
    path('category/<slug:category_slug>/', views.categories_by_slug, name='category_slug'),  # http://127.0.0.1:8000/category/1/
    # re_path(r"^archive/(?P<year>[0-9]{4})/", views.archive, name='archive') # собственные конверторы
    path("archive/<year4:year>/", views.archive, name='archive'),  # собственные конверторы
]
