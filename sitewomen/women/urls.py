from django.http import HttpRequest, HttpResponseNotFound

from . import converters

from django.urls import path, register_converter
from . import views

register_converter(converters.FourDigitYearConverter, 'year4')

urlpatterns = [
    path('', views.index, name='home'),
    path('about/',views.about, name='about'),
    path('post/<int:post_id>',views.show_post,name="post"),
    path('addpage/',views.addpage, name="addpage"),
    path('contact/',views.contact,name='contact'),
    path('login/',views.login,name='login'),
    path('category/<int:cats_id>',views.show_category, name='category')
]


def page_not_found(request, exception):
    return HttpResponseNotFound("<h1>Страница не найдена</h1>")
