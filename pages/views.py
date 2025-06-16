from django.shortcuts import render
from django.urls import reverse
from django.conf import settings
from listings.models import two_dish_rice

# Create your views here.
def index(request):
    # Get first 10 listings for the carousel
    featured_listings = two_dish_rice.objects.filter(restaurant_photo_main__isnull=False).exclude(restaurant_photo_main='')[:10]
    
    context = {
        'google_maps_api_key': settings.GOOGLE_MAPS_API_KEY,
        'featured_listings': featured_listings
    }
    return render(request,'pages/index.html', context)

def about(request):
    return render(request,'pages/about.html')