from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
from foodie.choices import gender_choices, age_range_choices, occupation_choices, live_district_choices


# Create your models here.

class Contact(models.Model):
    user = models.OneToOneField(User, on_delete=models.DO_NOTHING)
    foodie_name = models.CharField(max_length=200)
    updated_date = models.DateTimeField(auto_now=True)
    gender = models.CharField(max_length=10, choices=gender_choices.items())
    age_range=models.CharField(max_length=10, choices=age_range_choices.items())
    occupation=models.CharField(max_length=20, choices=occupation_choices.items())
    live_district=models.CharField(max_length=50, choices=live_district_choices.items())
    favor_chinese = models.BooleanField(default=False)
    favor_western = models.BooleanField(default=False)
    favor_veg = models.BooleanField(default=False)
    favor_organic = models.BooleanField(default=False)
    favor_japan = models.BooleanField(default=False)
    favor_korean = models.BooleanField(default=False)
    favor_thai = models.BooleanField(default=False)
    favor_seafood = models.BooleanField(default=False)
    favor_muslim = models.BooleanField(default=False)
    favor_no_beef = models.BooleanField(default=False)
    favor_no_pork = models.BooleanField(default=False)
    foodie_desc = models.CharField(max_length=200)
    foodie_photo = models.ImageField(upload_to='foodie_photos/', blank=True)
    is_mvp = models.BooleanField(default=False)



    def __str__(self):
        return self.foodie_name
