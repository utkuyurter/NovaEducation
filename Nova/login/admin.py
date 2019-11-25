from django.contrib import admin
from .models import *
# Register your models here.
admin.site.site_header = "Nova Education Administration"
admin.site.index_title = "Nova Education"
admin.site.site_title = "Nova Admin"

#admin.site.register(Person)
admin.site.register(Student)
admin.site.register(Teacher)
admin.site.register(Classes)
admin.site.register(Content)
admin.site.register(Reminder)
admin.site.register(Grade)
admin.site.register(ContentGrade)
