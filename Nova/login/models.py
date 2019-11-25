from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class Teacher(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=50, null=True)
    last_name = models.CharField(max_length=50, null=True)
    nova_id = models.IntegerField(null=True)
    school = models.CharField(max_length=50, null=True)
    department = models.CharField(max_length=50, null=True)
    teacher_id = models.IntegerField(null=True)

class Content(models.Model):
    id = models.AutoField(primary_key=True)
    teacher = models.IntegerField(null=True)
    type = models.CharField(null=True,max_length=50)
    class_id = models.CharField(max_length=50, null=True)
    title = models.CharField(max_length=50, null=True)
    desc = models.CharField(max_length=50, null=True)
    due_date = models.CharField(max_length=50, null=True)
    due_time = models.CharField(max_length=50, null=True)
    total_submissions = models.IntegerField(null=True)
    missing_submissions = models.IntegerField(null=True)
    affect = models.IntegerField(null=True)


class Classes(models.Model):
    id = models.AutoField(primary_key=True)
    class_id = models.CharField(max_length=50, null=True)
    class_section = models.CharField(max_length=50, null=True)
    class_name = models.CharField(max_length=50, null=True)
    class_number = models.IntegerField(null=True)
    class_teacher = models.CharField(max_length=50, null=True)
    class_teacher_number = models.IntegerField(null=True)
    class_credits = models.IntegerField(null=True)
    class_desc = models.CharField(max_length=50, null=True)
    class_day = models.CharField(max_length=50, null=True)
    class_times = models.CharField(max_length=50, null=True)
    contents = models.ForeignKey(Content, on_delete=models.CASCADE)

    def days(self):
        a = self.class_day.split("-")
        return a

    def times(self):
        a = self.class_times.split("-")
        return a


class ContentGrade(models.Model):
    id = models.AutoField(primary_key=True)
    student_id = models.CharField(max_length=50, null=True)
    content_of = models.ForeignKey(Content, on_delete=models.CASCADE)
    grade_letter = models.CharField(max_length=50, null=True)
    grade_number = models.CharField(max_length=50, null=True)



class Grade(models.Model):
    id = models.AutoField(primary_key=True)
    student_id = models.CharField(max_length=50, null=True)
    class_of = models.ForeignKey(Classes, on_delete=models.CASCADE)
    grade_letter = models.CharField(max_length=50, null=True)
    grade_number = models.CharField(max_length=50, null=True)


class Student(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=50, null=True)
    last_name = models.CharField(max_length=50, null=True)
    nova_id = models.CharField(max_length=50, null=True)
    school = models.CharField(max_length=50, null=True)
    student_id = models.CharField(max_length=50, null=True)
    gpa = models.DecimalField(max_digits=3, decimal_places=2, null=True)
    gpa_projected = models.DecimalField(max_digits=3, decimal_places=2, null=True)
    credits_taken = models.IntegerField(null=True)
    credits_current = models.IntegerField(null=True)
    classes = models.ManyToManyField(Classes)
    major = models.CharField(max_length=50, null=True)
    grades = models.ManyToManyField(Grade)



class Reminder(models.Model):
    id = models.AutoField(primary_key=True)
    reminder_title = models.CharField(max_length=50, null=True)
    reminder_message = models.CharField(max_length=200, null=True)
    reminder_id = models.CharField(max_length=100, null=True)

    def only_id(self):
        a = self.reminder_id.split("+")
        return a
