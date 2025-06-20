from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from listings.models import two_dish_rice
from comments.models import comment_rate, CommentRating
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from listings.choices import area_choices, district_choices
from django.contrib import messages
from django.db.models import Avg
import json
from django.contrib.auth import authenticate, login # 导入 authenticate 和 login
from django.contrib.auth.forms import AuthenticationForm # 导入 Django 内置的登录表单


def listing(request,listing_id):
    listing = get_object_or_404(two_dish_rice,pk=listing_id)
    comments = comment_rate.objects.filter(two_dish_rice_id=listing_id).order_by('-list_date')
    
    # 為每個評論計算其獲得的平均評分
    comments_with_ratings = []
    for comment in comments:
        # 計算這個特定評論獲得的所有評分的平均值
        avg_rating = CommentRating.objects.filter(
            comment=comment
        ).aggregate(avg_rating=Avg('rating'))['avg_rating']
        
        comment_data = {
            'comment': comment,
            'avg_comment_rating': round(avg_rating, 1) if avg_rating else None
        }
        comments_with_ratings.append(comment_data)
    
    context = {
        "listing": listing, 
        "comments": comments,
        "comments_with_ratings": comments_with_ratings
    }
    return render(request, 'listings/listing.html', context)


def search(request):
    queryset_list = two_dish_rice.objects.order_by('-list_date')

    if 'restaurant_area' in request.GET:
        restaurant_area = request.GET['restaurant_area']
        if restaurant_area:
            queryset_list = queryset_list.filter(restaurant_area__iexact=restaurant_area)
    if 'restaurant_district' in request.GET:
        restaurant_district = request.GET['restaurant_district']
        if restaurant_district:
            queryset_list = queryset_list.filter(restaurant_district__iexact=restaurant_district)
    if 'restaurant_street' in request.GET:
        restaurant_street = request.GET['restaurant_street']
        if restaurant_street:
            queryset_list = queryset_list.filter(restaurant_street__icontains=restaurant_street)
    if 'restaurant_name' in request.GET:
        restaurant_name = request.GET['restaurant_name']
        if restaurant_name:
            queryset_list = queryset_list.filter(restaurant_name__icontains=restaurant_name)
    if 'category_chinese' in request.GET:
        category_chinese = request.GET['category_chinese']
        if category_chinese:
            queryset_list = queryset_list.filter(category_chinese=True)
    if 'category_western' in request.GET:
        category_western = request.GET['category_western']
        if category_western:
            queryset_list = queryset_list.filter(category_western=True)
    if 'category_seafood' in request.GET:
        category_seafood = request.GET['category_seafood']
        if category_seafood:
            queryset_list = queryset_list.filter(category_seafood=True)       
    if 'category_veg' in request.GET:
        category_veg = request.GET['category_veg']
        if category_veg:
            queryset_list = queryset_list.filter(category_veg=True)   
    if 'category_japan' in request.GET:
        category_japan = request.GET['category_japan']
        if category_japan:
            queryset_list = queryset_list.filter(category_japan=True)   

    context = {"area_choices": area_choices, "district_choices": district_choices 
               , "listings": queryset_list, "values": request.GET}
    return render(request, 'listings/search.html', context)




def add_restaurant(request):
    if request.method == 'POST':
        try:
            # 从POST数据中获取所有字段值
            data = request.POST

            # 处理营业时间 - 只保存被选中的时段
            time_fields = {
                'fullday': ('openhour_fullday', 'closehour_fullday'),
                'afternoon': ('openhour_afternoon', 'closehour_afternoon'),
                'night': ('openhour_night', 'closehour_night'),
                'nightsnack': ('openhour_nightsnack', 'closehour_nightsnack'),
            }
            
            time_values = {}
            for period, (open_field, close_field) in time_fields.items():
                if period in data:  # 如果时段被选中
                    time_values[open_field] = data.get(open_field, None)
                    time_values[close_field] = data.get(close_field, None)
                else:  # 如果时段未被选中，设为None
                    time_values[open_field] = None
                    time_values[close_field] = None
            
            # 创建新记录
            new_restaurant = two_dish_rice(
                restaurant_name=data.get('restaurant_name', ''),
                restaurant_area=data.get('restaurant_area', ''),
                restaurant_district=data.get('restaurant_district', ''),
                restaurant_street=data.get('restaurant_street', ''),
                restaurant_address=data.get('restaurant_address', ''),
                fullday='fullday' in data,
                afternoon='afternoon' in data,
                night='night' in data,
                nightsnack='nightsnack' in data,
                # 使用处理后的时间值
                openhour_fullday=time_values['openhour_fullday'],
                closehour_fullday=time_values['closehour_fullday'],
                openhour_afternoon=time_values['openhour_afternoon'],
                closehour_afternoon=time_values['closehour_afternoon'],
                openhour_night=time_values['openhour_night'],
                closehour_night=time_values['closehour_night'],
                openhour_nightsnack=time_values['openhour_nightsnack'],
                closehour_nightsnack=time_values['closehour_nightsnack'],
                category_chinese='category_chinese' in data,
                category_western='category_western' in data,
                category_seafood='category_seafood' in data,
                category_veg='category_veg' in data,
                category_japan='category_japan' in data,
                menu=data.get('menu', ''),
                two_dish_price=int(data.get('two_dish_price', 0) or 0),
                three_dish_price=int(data.get('three_dish_price', 0) or 0),
                drink_price=int(data.get('drink_price', 0) or 0),
                soup_price=int(data.get('soup_price', 0) or 0),
                payment_cash='payment_cash' in data,
                payment_octopus='payment_octopus' in data,
                payment_alipayhk='payment_alipayhk' in data,
                payment_wechatpay='payment_wechatpay' in data,
                payment_payeme='payment_payeme' in data,
                dine_in='dine_in' in data,
                takeaway='takeaway' in data,
                takeaway_self='takeaway_self' in data,
                takeaway_keeta='takeaway_keeta' in data,
                takeaway_foodpanda='takeaway_foodpanda' in data,
                is_published= False,
                discount_coupon='discount_coupon' in data,
                
                # 自动设置日期
                list_date=timezone.now(),
                edit_date=timezone.now().date()
            )
            
            # 处理图片上传
            if 'restaurant_photo_main' in request.FILES:
                new_restaurant.restaurant_photo_main = request.FILES['restaurant_photo_main']
            
            for i in range(1, 7):
                field_name = f'menu_photo{i}'
                if field_name in request.FILES:
                    setattr(new_restaurant, field_name, request.FILES[field_name])
            
            # 保存到数据库
            new_restaurant.save()
            
            # 添加成功消息
            messages.success(request, '多謝你添加餐廳，管理員會盡快批核餐廳資料！')
            
            # 重定向到成功页面
            return redirect("pages:index")
        
        except Exception as e:
            # 在实际应用中，这里应该有更详细的错误处理
            return render(request, 'listings/add_restaurant.html', {
                'error_message': f'保存失败: {str(e)}',
                'form_data': json.dumps(data),  # 保存表单数据用于回填
            })
    
    # GET请求时显示空表单
    return render(request, 'listings/add_restaurant.html')

def success_page(request):
    return render(request, 'success.html')


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                return redirect('pages:index')  # 登录成功后重定向到首页
            else:
                messages.error(request,"Invalid username or password.")
        else:
            messages.error(request,"Invalid username or password.")
    form = AuthenticationForm()
    return render(request, 'listings/login.html', {'form': form})


# Create your views here.


# Create your views here.
