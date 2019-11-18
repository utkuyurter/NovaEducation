from django.urls import path

from . import views


urlpatterns = [
    path('class_assignment/', views.classAssignments, name='assignments'),
    path('class_quizzes/', views.classQuizzes, name='quizzes'),
    path('class_tests/', views.classTests, name='tests'),
    path('class_projects/', views.classProjects, name='projects'),
]
