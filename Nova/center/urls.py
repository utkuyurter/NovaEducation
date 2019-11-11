from django.urls import path

from . import views

urlpatterns = [
    path('', views.center, name='center'),
    path('student_center/', views.studentCenter, name='studentCenter'),
]
