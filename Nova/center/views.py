from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
# Create your views here.


def center(request):
    return HttpResponse("Center")

def studentCenter(request):
    template = loader.get_template('center/land_student.html')
    context = {
    }
    return HttpResponse(template.render(context, request))

def teacherCenter(request):
    template = loader.get_template('center/land_teacher.html')
    context = {
    }
    return HttpResponse(template.render(context, request))

def studentClass(request):
    template = loader.get_template('center/student_class.html')
    context = {
    }
    return HttpResponse(template.render(context, request))

def teacherClass(request):
    template = loader.get_template('center/teacher_class.html')
    context = {
    }
    return HttpResponse(template.render(context, request))

def teacherClassSettings(request):
    template = loader.get_template('center/course_settings.html')
    context = {
    }
    return HttpResponse(template.render(context, request))
