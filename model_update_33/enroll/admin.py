from django.contrib import admin
from enroll.models import RegistrationForm
# Register your models here.

@admin.register(RegistrationForm)
class RegistrationFormAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'email', 'password']