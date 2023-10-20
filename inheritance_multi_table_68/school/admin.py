from django.contrib import admin
from .models import ExamCenter, Student

# ExamCenter Register your models here.
@admin.register(ExamCenter)
class ExamCenterAdmin(admin.ModelAdmin):
    list_display = ['id', 'cname', 'city']


# ExamCenter Register your models here.
@admin.register(Student)
class ExamCenterAdmin(admin.ModelAdmin):
    list_display = ['id', 'cname', 'city', 'name', 'roll']
