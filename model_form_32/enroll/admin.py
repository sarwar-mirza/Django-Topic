from django.contrib import admin
from enroll.models import StudentDatabase
# Register your models here.

@admin.register(StudentDatabase)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'email', 'password']
