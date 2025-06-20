from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from foodie.models import Contact
from django.contrib import messages
from django.db import IntegrityError

@login_required
def add_foodie(request):
    # 檢查用戶是否已經有 Contact 記錄
    try:
        existing_contact = Contact.objects.get(user=request.user)
        messages.info(request, "您已經有個人資料了，將導向編輯頁面。")
        return redirect('foodie:edit_foodie')
    except Contact.DoesNotExist:
        # 用戶沒有 Contact 記錄，可以創建新的
        pass
    
    if request.method == 'POST':
        foodie_name = request.POST.get('nickname')  # 修正欄位名稱
        gender = request.POST.get('gender', 'Male')  # 提供預設值
        age_range = request.POST.get('age_range')
        occupation = request.POST.get('occupation', 'other')  # 提供預設值
        live_district = request.POST.get('location')  # 修正欄位名稱
        
        # 處理飲食偏好 - 修正這裡
        food_preferences_str = request.POST.get('food_preferences', '')
        food_preferences = [pref.strip() for pref in food_preferences_str.split(',') if pref.strip()]
        
        favor_chinese = '中式' in food_preferences
        favor_western = '西式' in food_preferences
        favor_veg = '素食' in food_preferences
        favor_organic = '有機' in food_preferences
        favor_japan = '日式' in food_preferences
        favor_korean = '韓式' in food_preferences
        favor_thai = '泰式' in food_preferences
        favor_seafood = '海鮮' in food_preferences
        favor_muslim = '清真' in food_preferences
        favor_no_beef = '不吃牛肉' in food_preferences
        favor_no_pork = '不吃豬肉' in food_preferences
        
        foodie_desc = request.POST.get('bio', '')  # 修正欄位名稱並提供預設值
        foodie_photo = request.FILES.get('profile_photo')  # 修正欄位名稱
        
        try:
            new_foodie = Contact(
                user=request.user,
                foodie_name=foodie_name,
                gender=gender,
                age_range=age_range,
                occupation=occupation,
                live_district=live_district,
                favor_chinese=favor_chinese,
                favor_western=favor_western,
                favor_veg=favor_veg,
                favor_organic=favor_organic,
                favor_japan=favor_japan,
                favor_korean=favor_korean,
                favor_thai=favor_thai,
                favor_seafood=favor_seafood,
                favor_muslim=favor_muslim,
                favor_no_beef=favor_no_beef,
                favor_no_pork=favor_no_pork,
                foodie_desc=foodie_desc,
                foodie_photo=foodie_photo
            )
            
            new_foodie.save()
            messages.success(request, "個人資料已成功建立！")
            return redirect('pages:index')
        except IntegrityError:
            messages.error(request, "您已經有個人資料了，無法重複建立。")
            return redirect('foodie:edit_foodie')
    
    return render(request, 'foodie/add_foodie.html')


def view_foodie(request, foodie_id):
    try:
        foodie = Contact.objects.get(id=foodie_id)
        context = {
            'foodie': foodie
        }
        return render(request, 'foodie/view_foodie.html', context)
    except Contact.DoesNotExist:
        messages.error(request, "找不到該會員資料")
        return redirect('pages:index')

@login_required
def view_my_profile(request):
    try:
        foodie = Contact.objects.get(user=request.user)
        context = {
            'foodie': foodie
        }
        return render(request, 'foodie/view_foodie.html', context)
    except Contact.DoesNotExist:
        messages.error(request, "您尚未建立個人資料，請先建立。")
        return redirect('foodie:add_foodie')

@login_required
def edit_foodie(request):
    try:
        # 根據當前登入用戶獲取 foodie 資料
        foodie = Contact.objects.get(user=request.user)
    except Contact.DoesNotExist:
        messages.error(request, "您尚未建立個人資料，請先建立。")
        return redirect('foodie:add_foodie')
    
    if request.method == 'POST':
        # 更新資料的邏輯（與 add_foodie 類似）
        foodie.foodie_name = request.POST.get('nickname', foodie.foodie_name)
        foodie.gender = request.POST.get('gender', foodie.gender)
        foodie.age_range = request.POST.get('age_range', foodie.age_range)
        foodie.occupation = request.POST.get('occupation', foodie.occupation)
        foodie.live_district = request.POST.get('location', foodie.live_district)
        
        # 處理飲食偏好 - 修正這裡
        food_preferences_str = request.POST.get('food_preferences', '')
        food_preferences = [pref.strip() for pref in food_preferences_str.split(',') if pref.strip()]
        
        foodie.favor_chinese = '中式' in food_preferences
        foodie.favor_western = '西式' in food_preferences
        foodie.favor_veg = '素食' in food_preferences
        foodie.favor_organic = '有機' in food_preferences
        foodie.favor_japan = '日式' in food_preferences
        foodie.favor_korean = '韓式' in food_preferences
        foodie.favor_thai = '泰式' in food_preferences
        foodie.favor_seafood = '海鮮' in food_preferences
        foodie.favor_muslim = '清真' in food_preferences
        foodie.favor_no_beef = '不吃牛肉' in food_preferences
        foodie.favor_no_pork = '不吃豬肉' in food_preferences
        
        foodie.foodie_desc = request.POST.get('bio', foodie.foodie_desc)
        
        # 處理照片上傳
        if 'profile_photo' in request.FILES:
            foodie.foodie_photo = request.FILES['profile_photo']
        
        foodie.save()
        messages.success(request, "個人資料已成功更新！")
        return redirect('accounts:dashboard')
    
    # GET 請求：顯示編輯表單，預填現有資料
    context = {
        'foodie': foodie,
        'is_edit': True
    }
    return render(request, 'foodie/add_foodie.html', context)


