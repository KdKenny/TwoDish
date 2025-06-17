from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f"Welcome back, {username}!")
                # 登录成功后重定向到首页或用户仪表盘
                # 修改 'pages:index' 为您希望的重定向目标
                return redirect('pages:index') 
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/login.html', {'form': form})

# 如果您计划添加注册和登出视图，可以在这里实现它们
# def register_view(request):
#     # ... 注册逻辑 ...
#     pass

# def logout_view(request):
#     # ... 登出逻辑 ...
#     pass