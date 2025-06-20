from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User
from comments.models import comment_rate, CommentRating
from foodie.models import Contact
from django.shortcuts import render

def dashboard(request):
    try:
        # 獲取當前用戶的 Contact 記錄
        contact = Contact.objects.get(user=request.user)
        # 使用 Contact 的 ID 來查找評論
        user_contacts = comment_rate.objects.order_by('-two_dish_rice_id').filter(foodie_name_id=contact.id)
    except Contact.DoesNotExist:
        # 如果用戶沒有 Contact 記錄，顯示空的評論列表
        user_contacts = comment_rate.objects.none()
    
    context = {"comments": user_contacts}
    return render(request,'accounts/dashboard.html',context)

def register(request):
    if request.method == "POST":
        first_name = request.POST["first_name"]
        last_name = request.POST["last_name"]
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        if password == password2:
            if User.objects.filter(username=username).exists():
                messages.error(request, "Username already exists !")
                return redirect("accounts:register")
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request, "Email already exists !")
                    return redirect("accounts:register")
                else:
                    user = User.objects.create_user(username=username, password=password, email=email, first_name=first_name, last_name=last_name) 
                    user.save()
                    # 自動登入新註冊的用戶
                    auth.login(request, user)
                    messages.success(request, "Account created successfully")
                    return redirect("foodie:add_foodie")  
        else:
            messages.error(request, "Password do not match!")
            return render(request, 'accounts/register.html')
    else:
        return render(request, 'accounts/register.html')

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = auth.authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            messages.success(request, "You are now logged in !")
            return redirect("pages:index")
        else:
             messages.error(request, "Invalid credentials !")
             return redirect("accounts:login")
    else:
        return render(request,'accounts/login.html')

def logout(request):
    if request.method == "POST":
        auth.logout(request)
        messages.success(request, "You are now logged out.")
    return redirect("pages:index")



