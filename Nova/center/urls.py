from django.urls import path
from django.conf.urls import url

from . import views

app_name = "center"

urlpatterns = [
    path('', views.center, name='center'),
    url(r'^student_center/(?P<nm>[0-9]+)/$', views.studentCenter, name='studentCenter'),
    url(r'^teacher_center/(?P<nm>[0-9]+)/$', views.teacherCenter, name='teacherCenter'),
    url(r'^student_center/(?P<nm>[0-9]+)/reminder_complete/(?P<rm>[0-9]+)/$', views.reminderComplete, name='studentReminderComplete'),
    url(r'^student_center/(?P<nm>[0-9]+)/reminder_create/$', views.reminderCreate, name='studentReminderCreate'),
    #path('teacher_center/', views.teacherCenter, name='teacherCenter'),
    path('student_class/', views.studentClass, name='studentClass'),
    #path('teacher_class/', views.teacherClass, name='teacherClass'),
    url(r'^teacher_class/(?P<nm>[0-9]+)/(?P<tm>[0-9]+)/$', views.teacherClass, name='teacherClass'),
    url(r'^student_class/(?P<nm>[0-9]+)/(?P<sm>[0-9]+)/$', views.studentClass, name='studentClass'),
    url(r'^teacher_class/(?P<nm>[0-9]+)/(?P<sm>[0-9]+)/settings/$', views.teacherClassSettings, name='teacherClassSettings'),
    
]
