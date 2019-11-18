from django.urls import path

from . import views


urlpatterns = [
    path('class_assignment/', views.classAssignments, name='assignments'),
    path('class_quizzes/', views.classQuizzes, name='quizzes'),
    path('class_tests/', views.classTests, name='tests'),
    path('class_projects/', views.classProjects, name='projects'),
    path('class_quizzes/quiz/', views.classQuizzesQuiz, name='quiz'),
    path('class_assignment/assignment/', views.classAssignmentAssignment, name='assignment'),
    path('class_tests/test/', views.classTestsTest, name='test'),
    path('class_projects/project/', views.classProjectsProject, name='project'),
]
