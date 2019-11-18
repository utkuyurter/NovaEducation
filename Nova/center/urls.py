from django.urls import path

from . import views

urlpatterns = [
    path('', views.center, name='center'),
    path('student_center/', views.studentCenter, name='studentCenter'),
    path('teacher_center/', views.teacherCenter, name='teacherCenter'),
    path('student_class/', views.studentClass, name='studentClass'),
    path('teacher_class/', views.teacherClass, name='teacherClass'),
    path('teacher_class/settings/', views.teacherClassSettings, name='teacherClassSettings'),
]
