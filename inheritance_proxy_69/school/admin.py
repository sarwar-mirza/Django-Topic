from django.contrib import admin
from .models import ExamCenter, MyExamCenter

#Exam Center Register your models here.
@admin.register(ExamCenter)
class ExamCenterAdmin(admin.ModelAdmin):
    list_display = ['id', 'cname', 'city']


#Exam Center Register your models here.
@admin.register(MyExamCenter)
class MyExamCenterAdmin(admin.ModelAdmin):
    list_display = ['id', 'cname', 'city']
