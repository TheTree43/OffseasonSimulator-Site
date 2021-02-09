from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def Packers(request):
    return render(request, 'Packers.html')

def Bears(request):
    return render(request, 'Bears.html')

def Vikings(request):
    return render(request, 'Vikings.html')

def Lions(request):
    return render(request, 'Lions.html')
