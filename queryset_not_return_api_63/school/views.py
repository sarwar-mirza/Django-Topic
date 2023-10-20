from django.shortcuts import render
from .models import Student

# Create your views here.
def home(request):
    #student_data = Student.objects.get(pk=1)


    #student_data = Student.objects.first()
    #student_data = Student.objects.order_by('name').first()



    #student_data = Student.objects.last()



    #student_data = Student.objects.latest('pass_date')



    #student_data = Student.objects.all()
    #print(student_data.exists())

    #student_data = Student.objects.all()
    #one_data = Student.objects.get(pk=2)
    #print(student_data.filter(pk=one_data.pk).exists())



    #student_data = Student.objects.create(name='Samir', roll=111, city='Shirajgonj', marks=40, pass_date='2023-9-26')
    
    
    
    #student_data, created = Student.objects.get_or_create(name='Samir', roll=111, city='Shirajgonj', marks=40, pass_date='2023-9-26')
    #print(created)
    
    
    #student_data = Student.objects.filter(id=4).update(name='Rana', marks=80)
    
    
    
    #student_data, created = Student.objects.update_or_create(id=11, name='Samir', defaults={'name':'Kohli'})
    #print(created)
    



    #objs = [
    #    Student(name='Tishs', roll=112, city='Dhaka', marks=40, pass_date='2023-9-26'),
    #    Student(name='Orin', roll=113, city='Dhaka', marks=60, pass_date='2023-9-26')
    #]
    #student_data = Student.objects.bulk_create(objs)
  




    #all_student_data = Student.objects.all()
    #for stu in all_student_data:
    #    stu.city = 'Maijdee'
    #student_data = Student.objects.bulk_update(all_student_data, ['city'])

    
    # student_data = Student.objects.get(pk=12).delete()
    # student_data = Student.objects.filter(marks=60).delete()
    # student_data = Student.objects.all().delete()

    student_data = Student.objects.all()
    print(student_data.count())
    



 

    print("Return: ", student_data)
    
    return render(request, 'school/home.html', {'student': student_data})