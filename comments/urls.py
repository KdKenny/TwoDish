from django.urls import path
from . import views

app_name = 'comments'
urlpatterns = [
    path('addcomment', views.addcomment, name='addcomment'),
    # path('delcomment', views.delcomment, name='delcomment'),
    path('editcomment/<int:comment_id>', views.editcomment, name='editcomment'),
    path('deletecomment/<int:comment_id>', views.deletecomment, name='deletecomment'),
    # path('<int:comment_id>', views.viewcomment, name='viewcomment')
]