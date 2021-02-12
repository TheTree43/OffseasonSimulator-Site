from django.shortcuts import render
from .models import Thumbnail

def about(request):
    thumbnails = Thumbnail.objects
    return render(request, 'thumbnail/about.html', {'thumbnails':thumbnails})
