from django.db import models
'''
#Modify the initial Queryset
class CustomManager(models.Manager):
    def get_queryset(self):
        #return super().get_queryset().all()      #overriding Built-in method called when we call all()
        
        return super().get_queryset().order_by('name')      #overriding Built-in method called when we call all()
  '''  

#Add extra Manager
class CustomManager(models.Manager):
    def get_stu_roll_ranage(self, r1, r2):
        return super().get_queryset().filter(roll__range=(r1, r2))    #custom add extra manager & QuerySet lookup  
 