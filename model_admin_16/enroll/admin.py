from django.contrib import admin
from enroll.models import Student
# Register your models here.
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('id', 'stu_id', 'name', 'dept', 'email', 'pas')



#admin.site.register(Student, StudentAdmin)
