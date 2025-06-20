from django.shortcuts import render, get_object_or_404, redirect
from listings.models import two_dish_rice
from comments.models import comment_rate, CommentRating
from django.contrib import messages
from django.utils import timezone
import json
from comments.forms import CommentForm

def editcomment(request, comment_id):
    comment = get_object_or_404(comment_rate, pk=comment_id)
    if request.method == 'POST':  # 修復: request.meothd -> request.method, POST -> 'POST'
        form = CommentForm(request.POST, instance=comment)  # 修復: request,POST -> request.POST
        if form.is_valid():
            form.save()
            messages.success(request, '評論已成功更新！')
            return redirect('accounts:dashboard')  # 修復: redirect(request, ...) -> redirect(...)
    else:
        form = CommentForm(instance=comment)
    return render(request, 'comments/editcomment.html', {'form': form})

def deletecomment(request, comment_id):  
    comment = get_object_or_404(comment_rate, pk=comment_id)
    comment.delete()
    messages.success(request, '評論已成功刪除！')
    return redirect("accounts:dashboard")


def addcomment(request):
    if request.method == "POST":
        two_dish_rice_id = request.POST["listing_id"]
        restaurant = get_object_or_404(two_dish_rice, id=two_dish_rice_id)
        comment = request.POST["comment"]
        restaurant_rating = request.POST["restaurant_rating"]
        edit_date = timezone.now().date()

        # 在 comments/views.py 中修改第 36-42 行
        from foodie.models import Contact
        
        # 先定義 foodie_name_id 和 foodie_name
        if request.user.is_authenticated:
            try:
                # 獲取對應的 Contact 記錄
                contact = Contact.objects.get(user=request.user)
                foodie_name_id = contact.id  # 使用 Contact 的 ID
                foodie_name = contact.foodie_name  # 使用 Contact 的 foodie_name
            except Contact.DoesNotExist:
                # 重定向到建立 Contact 頁面，而不是使用 foodie_name_id = 0
                messages.warning(request, "請先完善您的個人資料")
                return redirect('foodie:add_foodie')
                # 如果用戶沒有 Contact 記錄，使用 User 資料
                foodie_name_id = 0
                foodie_name = f"{request.user.first_name} {request.user.last_name}"
        else:
            foodie_name_id = 0  # guest is 0
            foodie_name = "guest"

        # 檢查是否是評分評論的請求
        if "comment_rating" in request.POST and request.POST["comment_rating"]:
            # 這是評分評論的請求
            comment_rating_value = request.POST["comment_rating"]
            target_comment_id = request.POST.get("target_comment_id")
            
            if target_comment_id:
                target_comment = get_object_or_404(comment_rate, id=target_comment_id)
                
                # 檢查用戶是否已經評分過這個評論
                existing_rating = CommentRating.objects.filter(
                    comment=target_comment,
                    rater_id=foodie_name_id
                ).first()
                
                if existing_rating:
                    # 更新現有評分
                    existing_rating.rating = comment_rating_value
                    existing_rating.save()
                    messages.success(request, "您的評分已更新")
                else:
                    # 創建新評分
                    CommentRating.objects.create(
                        comment=target_comment,
                        rater_id=foodie_name_id,
                        rater_name=foodie_name,
                        rating=comment_rating_value
                    )
                    messages.success(request, "評分已提交")
        else:
            # 這是添加新評論的請求
            new_comments = comment_rate(
                two_dish_rice_id=two_dish_rice_id, 
                restaurant_name=restaurant.restaurant_name, 
                comment=comment, 
                foodie_name_id=foodie_name_id, 
                foodie_name=foodie_name, 
                edit_date=edit_date, 
                restaurant_rating=restaurant_rating
            )

            new_comments.save()
            messages.success(request, "您的評論已提交")
        
        return redirect("listings:listing", listing_id=two_dish_rice_id)
