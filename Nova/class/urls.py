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
    path('teacher_class_assignment/', views.teacherClassAssignments, name='teacherAssignments'),
    path('teacher_class_quizzes/', views.teacherClassQuizzes, name='teacherQuizzes'),
    path('teacher_class_tests/', views.teacherClassTests, name='teacherTests'),
    path('teacher_class_projects/', views.teacherClassProjects, name='teacherProjects'),
    path('teacher_class_assignment/settings/', views.contentSettings, name='teacherAssignmentsSettings'),
    path('teacher_class_quizzes/settings/', views.contentSettings, name='teacherQuizzesSettings'),
    path('teacher_class_tests/settings/', views.contentSettings, name='teacherTestsSettings'),
    path('teacher_class_projects/settings/', views.contentSettings, name='teacherProjectsSettings'),
    path('teacher_class_assignment/create/', views.contentCreate, name='teacherAssignmentsCreate'),
    path('teacher_class_quizzes/create/', views.contentCreate, name='teacherQuizzesCreate'),
    path('teacher_class_tests/create/', views.contentCreate, name='teacherTestsCreate'),
    path('teacher_class_projects/create/', views.contentCreate, name='teacherProjectsCreate'),


]
