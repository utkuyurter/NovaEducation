from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth.decorators import login_required
# Create your views here.
from login.models import Student, Teacher, Classes, Reminder, Grade, ContentGrade, Content
from django.http import HttpResponseRedirect
from random import seed
from random import randint
from datetime import datetime


def center(request):
    return HttpResponse("Center")

@login_required(login_url='/login/')
def studentCenter(request, nm):
    template = loader.get_template('center/land_student.html')
    student = Student.objects.filter(nova_id__contains=nm)
    classes = Grade.objects.filter(student_id__contains=nm)
    reminders = Reminder.objects.filter(reminder_id__contains=nm)
    contents = ContentGrade.objects.filter(student_id__contains=nm)


    if nm in request.user.username:
        context = {
            'student' : student,
            'classes' : classes,
            'reminders' : reminders,
            'contents' : contents,

            }
        return HttpResponse(template.render(context, request))
    else:
        id = request.user.username.split("@")
        id_nova = id[1]
        print(id_nova)
        student = Student.objects.filter(nova_id__contains=nm)
        context = {
            'student' : student,
            'classes' : classes,
            'reminders' : reminders,

            }
        return HttpResponse(template.render(context, request))

@login_required(login_url='/login/')
def teacherCenter(request, nm):
    template = loader.get_template('center/land_teacher.html')
    teacher = Teacher.objects.filter(nova_id__contains=nm)
    classes = Classes.objects.filter(class_teacher_number__contains=nm)
    context = {
        'teacher' : teacher,
        'classes' : classes,
    }
    if request.method == 'POST':
        subject = request.POST['subject']
        to = request.POST['to']
        message = request.POST['message']


        return HttpResponse(template.render(context, request))
    return HttpResponse(template.render(context, request))

@login_required(login_url='/login/')
def studentClass(request, nm, sm):
    template = loader.get_template('center/student_class.html')
    class_of = Grade.objects.filter(class_of__class_id__contains=nm, student_id=sm)
    student = Student.objects.filter(nova_id__contains=sm)
    content = ContentGrade.objects.filter(student_id__contains=sm, content_of__class_id__contains=nm)

    # assignments = ContentGrade.objects.filter(content_of_id__contains=nm, content_of_type__contains="Assignment")
    # tests = ContentGrade.objects.filter(content_of_id__contains=nm, content_of_type__contains="Test")
    # quizzes = ContentGrade.objects.filter(content_of_id__contains=nm, content_of_type__contains="Quiz")
    # projects = ContentGrade.objects.filter(content_of_id__contains=nm, content_of_type__contains="Project")

    context = {
        'student' : student,
        'class' : class_of,
        'content' : content,
    }
    return HttpResponse(template.render(context, request))

@login_required(login_url='/login/')
def teacherClass(request, nm, tm):
    template = loader.get_template('center/teacher_class.html')
    class_of = Classes.objects.filter(class_id__contains=nm)
    teacher = Teacher.objects.filter(nova_id__contains=tm)
    content = Content.objects.filter(class_id__contains=nm, teacher=tm)
    num_student = len(Grade.objects.filter(class_of__class_id__contains=nm))
    context = {
        'teacher' : teacher,
        'class' : class_of,
        'num_student': num_student,
        'content' : content,
    }
    return HttpResponse(template.render(context, request))

@login_required(login_url='/login/')
def teacherClassSettings(request, nm, sm):
    template = loader.get_template('center/course_settings.html')
    course = Classes.objects.filter(class_id__contains=nm)
    context = {
    }
    return HttpResponse(template.render(context, request))

@login_required(login_url='/login/')
def reminderComplete(request, nm, rm):
    reminder = Reminder.objects.filter(reminder_id__contains=rm+"+"+nm)
    print(rm+nm)
    reminder.delete()
    return HttpResponseRedirect("/center/student_center/"+nm+"/")


@login_required(login_url='/login/')
def reminderCreate(request, nm):
    template = loader.get_template('class/reminder_create.html')
    context = {
    }
    if request.method == 'POST':
        title = request.POST['title']
        reminder = request.POST['reminder']
        new_reminder = Reminder.objects.create(reminder_title = title, reminder_message = reminder)
        while(new_reminder.reminder_id == None):
            seed(datetime.now())
            id = str(randint(1,1000))
            if(not Reminder.objects.filter(reminder_id__contains=id).exists()):
                new_reminder.reminder_id = id+"+"+nm
                break
            else:
                continue
        new_reminder.save()
        return HttpResponseRedirect("/center/student_center/"+nm)

    return HttpResponse(template.render(context, request))
