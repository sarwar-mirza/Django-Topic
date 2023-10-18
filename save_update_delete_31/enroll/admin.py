from django.contrib import admin
from enroll.models import User
# Register your models here.

@admin.register(User)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'email', 'password', 're_password']
