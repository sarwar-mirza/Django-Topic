from django.db import models
from .managers import CustomManager

# Student models here.
class Student(models.Model):
    name = models.CharField(max_length=70)
    roll = models.IntegerField()


# ProxyStudent models here.
class ProxyStudent(Student):
    students = CustomManager()       #Custom Manager
    class Meta:
        proxy = True
        ordering = ['name']

    

