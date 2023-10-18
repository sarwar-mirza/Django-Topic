from django.db import models

# Create your models here.
class Student(models.Model):
    stu_id = models.IntegerField()
    stu_name = models.CharField(max_length=70)
    stu_dept = models.CharField(max_length=70)
    stu_email = models.EmailField(max_length=70)
    stu_pass = models.CharField(max_length=70)

    # admin panele object hisabe data dekhacche kinthu amra Name onujai dekthe cai 
    def __str__(self):
        return self.stu_name
    
    #jodi kon integer value di ta hole error dekabe stu_id.  intger ke convert kore nite hobe strine str(self.stu_id)
