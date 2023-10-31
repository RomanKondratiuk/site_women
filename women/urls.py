from django.urls import path, re_path, register_converter

from . import views
from . import converters

register_converter(converters.FourDigitYearConverter, "year4")


urlpatterns = [
    path('', views.index),  # http://127.0.0.1:8000
    path('category/<int:category_id>/', views.categories),  # http://127.0.0.1:8000/category/1/
    path('category/<slug:category_slug>/', views.categories_by_slug),  # http://127.0.0.1:8000/category/1/
    # re_path(r"^archive/(?P<year>[0-9]{4})/", views.archive) # собственные конверторы
    path("archive/<year4:year>/", views.archive), # собственные конверторы
]
