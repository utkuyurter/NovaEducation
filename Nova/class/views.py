from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
# Create your views here.
from login.models import Grade, ContentGrade, Content



def content(request, nm, tm, sm):
    content = ContentGrade.objects.get(id__contains=nm)
    type = content.content_of.type
    contents = ContentGrade.objects.filter(content_of__type__contains=type, student_id__contains=sm)
    single_content = ContentGrade.objects.filter(id__contains=nm, content_of__type__contains=type)
    template = loader.get_template('class/mainContent.html')
    student = request.user.username.split("@")
    context = {
        'student' : student,
        'contents' : contents,
        's_content' : single_content,
    }
    return HttpResponse(template.render(context, request))

def contentGroup(request, nm, sm, rm):
    content = ContentGrade.objects.get(id__contains=sm)
    type = content.content_of.type
    contents = ContentGrade.objects.filter(content_of__type__contains=type, content_of__class_id__contains=nm, student_id__contains=rm)
    single_content = ContentGrade.objects.filter(id__contains=sm, content_of__type__contains=type)
    template = loader.get_template('class/assignment_page.html')
    context = {
        'contents' : contents,
        'content' : content,
        's_content' : single_content,
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

def contentSubmissions(request):
    template = loader.get_template('class/submissions.html')
    context = {
    }
    return HttpResponse(template.render(context, request))

def contentSubmissionsGrade(request):
    template = loader.get_template('class/grade.html')
    context = {
    }
    return HttpResponse(template.render(context, request))

def teacherClassAttendance(request):
    template = loader.get_template('class/attendance.html')
    context = {
    }
    return HttpResponse(template.render(context, request))
