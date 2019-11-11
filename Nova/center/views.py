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
