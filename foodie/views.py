from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from .forms import RegistrationForm

# Create your views here.
def register_view(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            login(request, form.save())
            return redirect(request, "foodie:dashboard")
    else:
        form = UserCreationForm()
    return render(request, "foodie/register.html", { "form": form})

def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect("foodie:dashboard")
    else:
        form = AuthenticationForm()
    return render(request, "foodie/login.html", {"form": form})

def logout_view(request):
    if request.method == "POST":
        logout(request)
        return redirect("foodie:dashboard")
    return redirect("foodie:login")

def success_view(request):
    return render(request, "foodie/success.html")

@login_required
def dashboard_view(request):
    return render(request, "foodie/dashboard.tmal", {"user": request.user})

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('foodie:home')  # Replace with your desired redirect URL
    else:
        form = RegistrationForm()
    return render(request, 'register.html', {'form': form})