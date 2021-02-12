from django.shortcuts import render

# Create your views here.
def Packers(request):
    return render(request, 'flowchart/Packers.html')

def Bears(request):
    return render(request, 'flowchart/Bears.html')

def Vikings(request):
    return render(request, 'flowchart/Vikings.html')

def Lions(request):
    return render(request, 'flowchart/Lions.html')
