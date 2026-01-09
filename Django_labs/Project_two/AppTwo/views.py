#from django.http import HttpResponse

#def index(request):
#   return HttpResponse("<em>My Second App</em>")

from django.shortcuts import render

def index(request):
    context = {
        'welcome_message': 'Welcome to My Page',
        'course_name': 'Django Basics',
        'students_today': 25,
        'my_name': 'Apeksha'
    }
    return render(request, 'AppTwo/index.html', context)
