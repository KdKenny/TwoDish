from django.urls import path
from . import views

app_name = 'listings'
urlpatterns = [
    path('<int:listing_id>', views.listing, name='listing'),
    path('search', views.search, name='search'),
    path('add_restaruant', views.add_restaurant, name='add_restaurant')
]