from django.http import HttpRequest, HttpResponseNotFound

from . import converters

from django.urls import path, register_converter
from . import views

register_converter(converters.FourDigitYearConverter, 'year4')

urlpatterns = [
    # path('', views.index, name='home'),
    path('', views.WomenHome.as_view(), name='home'),
    path('about/', views.about, name='about'),
    path('post/<slug:post_slug>', views.ShowPost.as_view(), name="post"),
    # path('addpage/', views.addpage, name="addpage"),
    path('addpage/', views.AddPage.as_view(), name="addpage"),
    path('contact/', views.contact, name='contact'),
    path('login/', views.login, name='login'),
    # path('category/<slug:cat_slug>/', views.show_category, name='category'),
    path('category/<slug:cat_slug>/', views.WomenCategory.as_view(),name='category'),
    path('tag/<slug:tag_slug>', views.TagPostList.as_view(), name='tag')
]


def page_not_found(request, exception):
    return HttpResponseNotFound("<h1>Страница не найдена</h1>")
