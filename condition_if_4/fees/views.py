from django.shortcuts import render

# Create your views here.
def fees_django(request):
    student = {'names': ['Sarwar', 'Tumpa', 'Liza', 'Sadiya', 'Pinkey']}
    return render(request, 'fees/feesone.html', student)

def fees_python(request):
    student = {'names': ['Sarwar', 'Tumpa', 'Liza', 'Sadiya', 'Pinkey']}
    return render(request, 'fees/feestwo.html', student)

def fees_nested(request):
    stu = {'stu1':{'name': 'Sarwar mithu', 'roll': 101},
           'stu2':{'name': 'Tumpa Islam', 'roll': 102},
           'stu3':{'name': 'Sadiya Hoque', 'roll': 103},
           'stu4':{'name': 'Liza Sultana', 'roll': 104},
           'stu5':{'name': 'Pinkey Taluqdar', 'roll': 105},
           'stu6':{'name': 'Tisha', 'roll': 106},
           }
    students = {'student': stu}
    return render(request, 'fees/feesthree.html', students)

