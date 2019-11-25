from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader, RequestContext
from .models import *
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponsePermanentRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
import json
from .models import Student, Teacher, Classes

# Create your views here.


def index(request):
    template = loader.get_template('login/index.html')
    context = {
    }
    return HttpResponse(template.render(context, request))


def login(request):
    template = loader.get_template('login/login.html')
    student = Student.objects.all()
    teacher = Teacher.objects.all()
    context = {
        'student' : student,
        'teacher' : teacher,
    }
    if request.method == 'POST':
          username = request.POST['username']
          password = request.POST['password']
          student = Student.objects.filter(nova_id__contains=username)
          teacher = Teacher.objects.filter(nova_id__contains=username)
          user = authenticate(username=username, password=password)
          if user is not None:
              if user.is_active:
                  auth_login(request,user)
                  #login(request)
                  # Redirect to index page
                  id_part = username.split("@")
                  username = id_part[1]
                  if "student" in id_part[0]:
                      return HttpResponseRedirect("../center/student_center/"+username)
                  else:
                      return HttpResponseRedirect("../center/teacher_center/"+username)

                  #dump = json.loads(json.dumps())

              else:
                  # Return a 'disabled account' error message
                  return redirect('center:studentCenter')
          else:
              # Return an 'invalid login' error message.
              print  ("invalid login details " + username + " " + password)
              return HttpResponseRedirect('../loginFalse/')
    else:
        # the login is a  GET request, so just show the user the login form.
        return HttpResponse(template.render(context, request))


# def logout(request):
#     template = loader.get_template('login/logout.html')
#     context = {
#     }
#     return HttpResponseRedirect('../../')

@login_required(login_url='/login/')
def loggingOut(request):
    template = loader.get_template('login/logout.html')
    context = {
    }
    auth_logout(request)
    return HttpResponse(template.render(context, request))



def loginFalse(request):
    template = loader.get_template('login/loginFalse.html')
    student = Student.objects.all()
    teacher = Teacher.objects.all()
    context = {
        'student' : student,
        'teacher' : teacher,
    }
    if request.method == 'POST':
          username = request.POST['username']
          password = request.POST['password']
          student = Student.objects.filter(nova_id__contains=username)
          teacher = Teacher.objects.filter(nova_id__contains=username)
          user = authenticate(username=username, password=password)
          if user is not None:
              if user.is_active:
                  auth_login(request,user)
                  #login(request)
                  # Redirect to index page
                  id_part = username.split("@")
                  username = id_part[1]
                  if "student" in id_part[0]:
                      return HttpResponseRedirect("../center/student_center/"+username)
                  else:
                      return HttpResponseRedirect("../center/teacher_center/"+username)

                  #dump = json.loads(json.dumps())

              else:
                  # Return a 'disabled account' error message
                  return redirect('center:studentCenter')
          else:
              # Return an 'invalid login' error message.
              print  ("invalid login details " + username + " " + password)
              return HttpResponseRedirect('../loginFalse/')
    else:
        # the login is a  GET request, so just show the user the login form.
        return HttpResponse(template.render(context, request))
