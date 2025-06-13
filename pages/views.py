from django.shortcuts import render
from django.urls import reverse

# Create your views here.
def index(request):
    return render(request,'pages/index.html')

def about(request):
    return render(request,'pages/about.html')