from django.shortcuts import render, get_object_or_404, redirect
from foodie.models import Contact
from django.contrib import messages


# Create your views here.

def view_foodie(request, foodie_id):
    view_foodie = Contact.objects.filter(user_id=foodie_id)
    context = {
        'view_foodie': view_foodie,
    }
    return render(request, 'foodie/view_foodie.html', context)


def edit_foodie(request, foodie_id):
    
    return redirect("pages:index")


def add_foodie(request,foodie_id):
    if request.method == 'POST':
        foodie_name = request.POST.get('foodie_name')
        gender = request.POST.get('gender')
        age_range = request.POST.get('age_range')
        occupation = request.POST.get('occupation')
        live_district = request.POST.get('live_district')
        favor_chinese = request.POST.get('favor_chinese') == 'on'
        favor_western = request.POST.get('favor_western') == 'on'
        favor_veg = request.POST.get('favor_veg') == 'on'
        favor_organic = request.POST.get('favor_organic') == 'on'
        favor_japan = request.POST.get('favor_japan') == 'on'
        favor_korean = request.POST.get('favor_korean') == 'on'
        favor_thai = request.POST.get('favor_thai') == 'on'
        favor_seafood = request.POST.get('favor_seafood') == 'on'
        favor_muslim = request.POST.get('favor_muslim') == 'on'
        favor_no_beef = request.POST.get('favor_no_beef') == 'on'
        favor_no_pork = request.POST.get('favor_no_pork') == 'on'
        foodie_desc = request.POST.get('foodie_desc')
        foodie_photo = request.FILES.get('foodie_photo')    
        user_id = request.POST.get('foodie.id')
      
    
    new_foodie = Contact(
        foodie_name = foodie_name,
        gender = gender,
        age_range = age_range,
        occupation = occupation,
        live_district = live_district,
        favor_chinese = favor_chinese,
        favor_western = favor_western,
        favor_veg = favor_veg,
        favor_organic = favor_organic,
        favor_japan = favor_japan,
        favor_korean = favor_korean,
        favor_thai = favor_thai,
        favor_seafood = favor_seafood,
        favor_muslim = favor_muslim,
        favor_no_beef = favor_no_beef,
        favor_no_pork = favor_no_pork,
        foodie_desc = foodie_desc,
        foodie_photo = foodie_photo,
        user_id = user_id
    )
    
    new_foodie.save()
    messages.succcess(request, "Foodie login successfully created!")



    return render(request, 'foodie/add_foodie.html')


