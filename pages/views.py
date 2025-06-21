from django.shortcuts import render
from django.urls import reverse
from django.conf import settings
from listings.models import two_dish_rice
from adminusers.models import Adminuser

# Create your views here.
def index(request):
    # Get first 10 listings for the carousel
    featured_listings = two_dish_rice.objects.filter(restaurant_photo_main__isnull=False).exclude(restaurant_photo_main='')[:10]
    
    context = {
        'google_maps_api_key': settings.GOOGLE_MAPS_API_KEY,
        'featured_listings': featured_listings
    }
    return render(request,'pages/index.html', context)

def about(request):
    admin_users = Adminuser.objects.all()
    context = {
        'admin_users': admin_users
    }
    return render(request,'pages/about.html', context)

def news(request):
    # emu news 
    news_data = [
        {
            'title': '兩餸飯文化節2024盛大開幕！',
            'date': '2024年12月15日',
            'summary': '一年一度的兩餸飯文化節正式開幕，超過100間餐廳參與，為期一個月的美食盛宴等您來品嚐！',
            'image': 'https://via.placeholder.com/400x250/FF6B6B/FFFFFF?text=兩餸飯文化節',
            'content': '今年的兩餸飯文化節以「傳統與創新」為主題，匯聚了香港各區最具特色的兩餸飯餐廳...'
        },
        {
            'title': '健康兩餸飯新趨勢：低鹽低油更美味',
            'date': '2024年12月10日',
            'summary': '越來越多餐廳推出健康版兩餸飯，在保持傳統口味的同時，更注重營養均衡和健康烹調。',
            'image': 'https://via.placeholder.com/400x250/4ECDC4/FFFFFF?text=健康兩餸飯',
            'content': '隨著健康飲食意識的提升，許多兩餸飯餐廳開始調整烹調方式...'
        },
        {
            'title': '兩餸飯外賣服務全面升級',
            'date': '2024年12月5日',
            'summary': '為配合現代生活節奏，多間兩餸飯餐廳推出全新外賣包裝和配送服務，讓您在家也能享受正宗兩餸飯。',
            'image': 'https://via.placeholder.com/400x250/45B7D1/FFFFFF?text=外賣服務',
            'content': '新的外賣包裝採用環保材料，確保食物保溫的同時也保護環境...'
        }
    ]
    
    # 優惠券數據
    coupons = [
        {
            'title': '新客戶專享',
            'discount': '8折優惠',
            'description': '首次訂餐享8折優惠',
            'code': 'NEW20',
            'expiry': '2024年12月31日',
            'color': 'bg-danger'
        },
        {
            'title': '週末特惠',
            'discount': '買二送一',
            'description': '週末訂餐買二送一',
            'code': 'WEEKEND',
            'expiry': '2024年12月30日',
            'color': 'bg-success'
        },
        {
            'title': '學生優惠',
            'discount': '9折優惠',
            'description': '學生憑證享9折優惠',
            'code': 'STUDENT10',
            'expiry': '2025年1月31日',
            'color': 'bg-info'
        }
    ]
    
    context = {
        'news_list': news_data,
        'coupons': coupons
    }
    return render(request, 'pages/news.html', context)