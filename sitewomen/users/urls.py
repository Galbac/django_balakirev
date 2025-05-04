from debug_toolbar.urls import app_name
from django.urls import path

from users import views

app_name = 'users'
urlpatterns = [
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout')
]
