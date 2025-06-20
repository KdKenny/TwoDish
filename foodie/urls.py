from django.urls import path
from . import views


app_name = 'foodie'

urlpatterns = [
    path('addfoodie/<int:foodie_id>', views.add_foodie, name='add_foodie'),
    path('viewfoodie/<int:foodie_id>', views.view_foodie, name='view_foodie')
]