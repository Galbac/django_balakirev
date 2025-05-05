from debug_toolbar.urls import app_name
from django.urls import path

from users import views

app_name = 'users'
urlpatterns = [
    path('login/', views.LoginUser.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout')
]
