from django.db import models

# Create your models here.
class Student(models.Model):
    stu_id = models.IntegerField()
    stu_name = models.CharField(max_length=70)
    stu_dept = models.CharField(max_length=70)
    stu_email = models.EmailField(max_length=70)
    stu_pass = models.CharField(max_length=70)
