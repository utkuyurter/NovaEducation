from django import template
from django.contrib.auth.models import User
register = template.Library()

from login.models import Content, Classes, Grade, ContentGrade




@register.filter
def updateClassGrade(value, args):
    assignments_total = 0
    quizzes_total = 0
    tests_total = 0
    projects_total = 0
    affect_assignments = 0
    affect_quizzes = 0
    affect_tests = 0
    affect_projects = 0
    arg_list = [arg.strip() for arg in args.split(',')]
    student_id = ''.join(arg_list[0])
    assignments = ContentGrade.objects.filter(content_of__class_id__contains=value, content_of__type__contains="Assignment", student_id=student_id)
    quizzes = ContentGrade.objects.filter(content_of__class_id__contains=value, content_of__type__contains="Quiz", student_id=student_id)
    tests = ContentGrade.objects.filter(content_of__class_id__contains=value, content_of__type__contains="Test", student_id=student_id)
    projects = ContentGrade.objects.filter(content_of__class_id__contains=value, content_of__type__contains="Project", student_id=student_id)
    for i in assignments:
        affect_assignment = int(i.content_of.affect) / 100
        assignments_total += int(i.grade_number)
    for i in quizzes:
        affect_quizzes = int(i.content_of.affect) / 100
        quizzes_total += int(i.grade_number)
    for i in tests:
        affect_tests = int(i.content_of.affect) / 100
        tests_total += int(i.grade_number)
    for i in projects:
        affect_projects = int(i.content_of.affect) / 100
        projects_total += int(i.grade_number)

    return (assignments_total * affect_assignments) + (quizzes_total * affect_quizzes) + (tests_total * affect_tests) + (projects_total * affect_projects)

@register.filter
def toGradeLetter(value):
    assignments_total = 0
    quizzes_total = 0
    tests_total = 0
    projects_total = 0
    affect_assignments = 0
    affect_quizzes = 0
    affect_tests = 0
    affect_projects = 0
    arg_list = [arg.strip() for arg in args.split(',')]
    student_id = ''.join(arg_list[0])
    assignments = ContentGrade.objects.filter(content_of__class_id__contains=value, content_of__type__contains="Assignment", student_id=student_id)
    quizzes = ContentGrade.objects.filter(content_of__class_id__contains=value, content_of__type__contains="Quiz", student_id=student_id)
    tests = ContentGrade.objects.filter(content_of__class_id__contains=value, content_of__type__contains="Test", student_id=student_id)
    projects = ContentGrade.objects.filter(content_of__class_id__contains=value, content_of__type__contains="Project", student_id=student_id)
    for i in assignments:
        affect_assignment = int(i.content_of.affect) / 100
        assignments_total += int(i.grade_number)
    for i in quizzes:
        affect_quizzes = int(i.content_of.affect) / 100
        quizzes_total += int(i.grade_number)
    for i in tests:
        affect_tests = int(i.content_of.affect) / 100
        tests_total += int(i.grade_number)
    for i in projects:
        affect_projects = int(i.content_of.affect) / 100
        projects_total += int(i.grade_number)

    number = (assignments_total * affect_assignments) + (quizzes_total * affect_quizzes) + (tests_total * affect_tests) + (projects_total * affect_projects)
    if(number >= 90):
        t = Grade.objects.get(class_of__class_id__contains=value, student_id=student_id)
        t.grade_letter = "A"
        t.save()
    if(number >= 80 and number < 90):
        t = Grade.objects.get(class_of__class_id__contains=value, student_id=student_id)
        t.grade_letter = "B"
        t.save()
    if(number >= 70 and number < 80):
        t = Grade.objects.get(class_of__class_id__contains=value, student_id=student_id)
        t.grade_letter = "C"
        t.save()
    if(number >= 60 and number < 70):
        t = Grade.objects.get(class_of__class_id__contains=value, student_id=student_id)
        t.grade_letter = "D"
        t.save()
    if(number < 60):
        t = Grade.objects.get(class_of__class_id__contains=value, student_id=student_id)
        t.grade_letter = "F"
        t.save()

    print(rade.objects.get(class_of__class_id__contains=value, student_id=student_id))
    return Grade.objects.get(class_of__class_id__contains=value, student_id=student_id)


@register.filter
def getClassName(value):
    class_name = Classes.objects.filter(class_id__contains=value)
    for i in class_name:
        return i.class_name

@register.filter
def getClassNumber(value):
    class_num = Classes.objects.filter(class_id__contains=value)
    for i in class_num:
        return i.class_number

@register.filter
def getClassDesc(value):
    class_num = Classes.objects.filter(class_id__contains=value)
    for i in class_num:
        return i.class_desc

@register.filter
def gradeNum(value, args):
    arg_list = [arg.strip() for arg in args.split(',')]
    id = ''.join(arg_list)
    class_grade = Grade.objects.filter(class_of__class_id__contains=value,student_id__contains=id)
    for i in class_grade:
        return i.grade_number


# @register.filter
# def getAvgContent(value, args):
#     arg_list = [arg.strip() for arg in args.split(',')]
#     id = ''.join(arg_list[0])
#     tot = 0
#     student_id = ''.join(arg_list[1])
#     print(student_id)
#     class_contents = ContentGrade.objects.filter(content_of__class_id__contains=value, content_of__type__contains=id, student_id=student_id)
#
#     for i in class_contents:
#         tot = tot + int(i.grade_number)
#
#     avg = tot / len(class_contents)
#     return round(avg, 2)

@register.simple_tag
def getAvg(student_id, class_id, content_id):
    tot = 0
    cont = ContentGrade.objects.get(id__contains=content_id)
    content_type = cont.content_of.type
    class_contents = ContentGrade.objects.filter(content_of__class_id__contains=class_id, content_of__type__contains=content_type, student_id=student_id)

    for i in class_contents:
        tot = tot + int(i.grade_number)

    if(len(class_contents) == 0):
        return 0
    else:
        avg = tot / len(class_contents)
        return round(avg, 2)


# @register.simple_tag
# def getClassGrade(student_id, content_id, class_id):
#     assignments = ContentGrade.objects.filter(content_of__class_id__contains=class_id, content_of__type__contains="Assignment", student_id=student_id)
#     quizzes = ContentGrade.objects.filter(content_of__class_id__contains=class_id, content_of__type__contains="Quiz", student_id=student_id)
#     test = ContentGrade.objects.filter(content_of__class_id__contains=class_id, content_of__type__contains="Test", student_id=student_id)
#     projects = ContentGrade.objects.filter(content_of__class_id__contains=class_id, content_of__type__contains="Project", student_id=student_id)
#     assignments_affect = ContentGrade.objects.get(content_id__contains=content_id)
#     a_a = assignments_affect.content_of.affect
#     quizzes_affect = ContentGrade.objects.filter(content_of__class_id__contains=class_id, content_of__type__contains="Quiz").content_of.affect
#     test_affect = ContentGrade.objects.filter(content_of__class_id__contains=class_id, content_of__type__contains="Test").content_of.affect
#     projects_affect = ContentGrade.objects.filter(content_of__class_id__contains=class_id, content_of__type__contains="Project").content_of.affect
#
#     print(assignments_affect)
