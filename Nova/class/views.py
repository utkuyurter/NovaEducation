from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
# Create your views here.


def classAssignments(request):
    template = loader.get_template('class/assignments.html')
    context = {
    }
    return HttpResponse(template.render(context, request))

def classQuizzes(request):
    template = loader.get_template('class/quizzes.html')
    context = {
    }
    return HttpResponse(template.render(context, request))

def classProjects(request):
    template = loader.get_template('class/projects.html')
    context = {
    }
    return HttpResponse(template.render(context, request))

def classTests(request):
    template = loader.get_template('class/tests.html')
    context = {
    }
    return HttpResponse(template.render(context, request))
