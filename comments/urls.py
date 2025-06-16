from django.urls import path
from . import views

app_name = 'comments'
urlpatterns = [
    path('addcomment', views.addcomment, name='addcomment'),
]