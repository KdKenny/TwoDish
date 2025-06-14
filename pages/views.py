from django.shortcuts import render
from django.urls import reverse
from django.conf import settings

# Create your views here.
def index(request):
    context = {
        'google_maps_api_key': settings.GOOGLE_MAPS_API_KEY
    }
    return render(request,'pages/index.html', context)

def about(request):
    return render(request,'pages/about.html')