from django.urls import path
from . import views

app_name = 'foodie'

urlpatterns = [
    path('addfoodie/', views.add_foodie, name='add_foodie'), 
    path('viewfoodie/<int:foodie_id>/', views.view_foodie, name='view_foodie'),
    path('myprofile/', views.view_my_profile, name='view_my_profile'),  # 新增
    path('editfoodie/', views.edit_foodie, name='edit_foodie'),
]