from django.urls import path
from . import views
from django.contrib import admin
form django.urls import path, include

app_name = "foodie"

urlpatterns = [
    path("register/", views.register_view, name="register"),
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
    path("success/", views.success_view, name="success"),
    path("admin/", admin.site.urls),
    path("", include("foodie.urls")),
    path('', views.home, name='home'),
]



from django.urls import path
from . import views

app_name = 'foodie'