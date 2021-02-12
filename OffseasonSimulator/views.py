from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def simulator(request):
    return render(request, 'simulator.html')
