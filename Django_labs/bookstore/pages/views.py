from django.shortcuts import render

def home(request):
    return render(request, 'pages/home.html')

def books(request):
    return render(request, 'pages/books.html')

def about(request):
    return render(request, 'pages/about.html')
