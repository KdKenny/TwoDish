from django.urls import path
from . import views

app_name = 'accounts'  # 定义应用命名空间

urlpatterns = [
    path('login/', views.login_view, name='login'),
    # 如果您计划添加注册和登出功能，可以在这里添加它们的URL
    # path('register/', views.register_view, name='register'),
    # path('logout/', views.logout_view, name='logout'),
]