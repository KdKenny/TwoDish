from django.db import models
from django.contrib.auth.models import User # Import the User model
from datetime import datetime

class FoodieInfo(models.Model):
    # Link to the auth_user table
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True, related_name='foodie_profile')
    foodie_name = models.CharField(max_length=150) # Should be unique if it's a username equivalent

    GENDER_CHOICES = [
        ('male', 'Male'),
        ('female', 'Female'),
    ]
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES, blank=True, null=True)

    AGE_RANGE_CHOICES = [
        ('1', '10-20'),
        ('2', '21-30'),
        ('3', '31-40'),
        ('4', '41-50'),
        ('5', '51-60'),
        ('6', '61-70'), # Added based on typical age ranges
        ('7', '71-80'), # Added based on typical age ranges
        ('8', 'Over 80'), # Added based on typical age ranges
    ]
    age_range = models.CharField(max_length=10, choices=AGE_RANGE_CHOICES, blank=True, null=True)

    OCCUPATION_CHOICES = [
        ('white_collar', '白領'),
        ('technician', '技工'),
        ('driver', '司機'),
        ('housewife', '主婦'),
        ('boss', '老闆'),
        ('other', '其他'),
    ]
    occupation = models.CharField(max_length=50, choices=OCCUPATION_CHOICES, blank=True, null=True)

    DISTRICT_CHOICES = {
        'Islands': 'Islands',
        'Kwai Tsing': 'Kwai Tsing',
        'North': 'North',
        'Sai Kung': 'Sai Kung',
        'Sha Tin': 'Sha Tin',
        'Tai Po': 'Tai Po',
        'Tuen Mun': 'Tuen Mun',
        'Tsuen Wan': 'Tsuen Wan',
        'Yuen Long': 'Yuen Long',
        'Kowloon City': 'Kowloon City',
        'Kwun Tong': 'Kwun Tong',
        'Sham Shui Po': 'Sham Shui Po',
        'Wong Tai Sin': 'Wong Tai Sin',
        'Yau Tsim Mong': 'Yau Tsim Mong',
        'Central & Western': 'Central & Western',
        'Eastern': 'Eastern',
        'Southern': 'Southern',
        'Wan Chai': 'Wan Chai'
    }
    live_district = models.CharField(max_length=50, choices=list(DISTRICT_CHOICES.items()), blank=True, null=True)

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

    foodie_desc = models.TextField(blank=True)
    foodie_photo = models.ImageField(upload_to='photos/foodie/%Y/%m/%d/', blank=True, null=True)

    is_mvp = models.BooleanField(default=False) # Determine by admin

    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.foodie_name

    class Meta:
        verbose_name = 'Foodie Profile'
        verbose_name_plural = 'Foodie Profiles'

# Remarks: this table is for register member
