from django.urls import path, include
from django.conf.urls import url

from . import views

urlpatterns = [

    url(r'^$', views.index, name='main'),
    path('login/', views.login, name='login'),
    path('loginFalse/', views.loginFalse, name='loginFalse'),
    url(r'^logout/$', views.loggingOut, name='logout'),
    #path('logout/', views.logout, name='logout'),
]
