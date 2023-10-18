from django.shortcuts import render

# Create your views here.
def fees_django(request):
    course_fees = {'course1': {'name': 'Django', 'fees': 45000},
                   'course2': {'name': 'Python', 'fees': 40000} }
    course_details = {'learn': course_fees}
    return render(request, 'fees/feesone.html', course_details)