from django.contrib import admin
from school.models import Student, Teacher

# Student Register your models here.
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'roll', 'city', 'marks', 'pass_date']


# Teacher Register your models here.
@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'employ', 'city', 'salary', 'join_date']