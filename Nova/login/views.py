from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.


def index(request):
    template = loader.get_template('login/index.html')
    context = {
    }
    return HttpResponse(template.render(context, request))


def login(request):
    template = loader.get_template('login/login.html')
    context = {
    }
    return HttpResponse(template.render(context, request))


def landing(request):
    template = loader.get_template('login/login.html')
    context = {
    }
    return HttpResponse(template.render(context, request))


def studentLogin(request):
    return HttpResponse("Student Login Page")


def teacherLogin(request):
    return HttpResponse("Teacher Login Page")
