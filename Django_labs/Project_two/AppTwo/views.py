#from django.http import HttpResponse

#def index(request):
#   return HttpResponse("<em>My Second App</em>")

from django.shortcuts import render
from .models import Student

def index(request):
    students = Student.objects.all()

    context = {
        'welcome_message': 'Welcome to Django Templates',
        'course_name': 'Django Basics',
        'students_today': students.count(),
        'my_name': 'Apeksha',
        'students': students
    }

    return render(request, 'AppTwo/index.html', context)


