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

def classQuizzesQuiz(request):
    template = loader.get_template('class/quiz_page.html')
    context = {
    }
    return HttpResponse(template.render(context, request))

def classTestsTest(request):
    template = loader.get_template('class/test_page.html')
    context = {
    }
    return HttpResponse(template.render(context, request))

def classAssignmentAssignment(request):
    template = loader.get_template('class/assignment_page.html')
    context = {
    }
    return HttpResponse(template.render(context, request))

def classProjectsProject(request):
    template = loader.get_template('class/project_page.html')
    context = {
    }
    return HttpResponse(template.render(context, request))


def teacherClassAssignments(request):
    template = loader.get_template('class/teacher_assignment_page.html')
    context = {
    }
    return HttpResponse(template.render(context, request))

def teacherClassQuizzes(request):
    template = loader.get_template('class/teacher_quiz_page.html')
    context = {
    }
    return HttpResponse(template.render(context, request))

def teacherClassProjects(request):
    template = loader.get_template('class/teacher_project_page.html')
    context = {
    }
    return HttpResponse(template.render(context, request))

def teacherClassTests(request):
    template = loader.get_template('class/teacher_test_page.html')
    context = {
    }
    return HttpResponse(template.render(context, request))

def contentSettings(request):
    template = loader.get_template('class/content_settings.html')
    context = {
    }
    return HttpResponse(template.render(context, request))

def contentCreate(request):
    template = loader.get_template('class/content_create.html')
    context = {
    }
    return HttpResponse(template.render(context, request))
