from django.db import models

# Create your models here.
class Student(models.Model):
    stu_id = models.IntegerField()
    name = models.CharField(max_length=70)
    dept = models.CharField(max_length=70)
    email = models.EmailField(max_length=70)
    pas = models.CharField(max_length=70)

    '''def __str__(self):
        return self.name'''
