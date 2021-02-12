from django.shortcuts import render
from .models import Flowchart
# Create your views here.
def Packers(request):
    flowchart = Flowchart.objects
    return render(request, 'flowchart/Packers.html', {'flowchart':flowchart})

def Bears(request):
    flowchart = Flowchart.objects
    return render(request, 'flowchart/Bears.html', {'flowchart':flowchart})

def Vikings(request):
    flowchart = Flowchart.objects
    return render(request, 'flowchart/Vikings.html', {'flowchart':flowchart})

def Lions(request):
    flowchart = Flowchart.objects
    return render(request, 'flowchart/Lions.html', {'flowchart':flowchart})
