from tkinter import N
from django.db import models
from django.utils import timezone
from datetime import datetime
from listings.choices import area_choices, district_choices

# Create your models here.

class two_dish_rice(models.Model):
    restaurant_name = models.CharField(max_length=200)
    list_date = models.DateTimeField(auto_now_add=True)
    edit_date = models.DateField(blank=True)
    restaurant_photo_main = models.ImageField(upload_to='photos/', blank=True)
    restaurant_area = models.CharField(max_length=50, choices=area_choices.items())
    restaurant_district = models.CharField(max_length=50, choices=district_choices.items())
    restaurant_street = models.CharField(max_length=200)
    restaurant_address = models.CharField(max_length=200)
    fullday = models.BooleanField(default=True)
    openhour_fullday = models.TimeField(null=True, blank=True)
    closehour_fullday = models.TimeField(null=True, blank=True)
    afternoon = models.BooleanField(default=True)
    openhour_afternoon = models.TimeField(null=True, blank=True)
    closehour_afternoon = models.TimeField(null=True, blank=True)
    night = models.BooleanField(default=True)
    openhour_night = models.TimeField(null=True, blank=True)
    closehour_night = models.TimeField(null=True, blank=True)
    nightsnack = models.BooleanField(default=True)
    openhour_nightsnack = models.TimeField(null=True, blank=True)
    closehour_nightsnack = models.TimeField(null=True, blank=True)
    category_chinese = models.BooleanField(default=True)
    category_western = models.BooleanField(default=True)
    category_seafood = models.BooleanField(default=True)
    category_veg = models.BooleanField(default=True)
    category_japan = models.BooleanField(default=True)
    menu = models.TextField(blank=True)
    menu_photo1 = models.ImageField(upload_to='photos/', blank=True)
    menu_photo2 = models.ImageField(upload_to='photos/', blank=True)
    menu_photo3 = models.ImageField(upload_to='photos/', blank=True)
    menu_photo4 = models.ImageField(upload_to='photos/', blank=True)
    menu_photo5 = models.ImageField(upload_to='photos/', blank=True)
    menu_photo6 = models.ImageField(upload_to='photos/', blank=True)
    two_dish_price = models.IntegerField()
    three_dish_price = models.IntegerField()
    drink_price = models.IntegerField()
    soup_price = models.IntegerField()
    payment_cash = models.BooleanField(default=True)
    payment_octopus = models.BooleanField(default=True) 
    payment_alipayhk = models.BooleanField(default=True)
    payment_wechatpay = models.BooleanField(default=True)
    payment_payeme = models.BooleanField(default=True)
    dine_in = models.BooleanField(default=True)
    takeaway = models.BooleanField(default=True)
    takeaway_self = models.BooleanField(default=True)
    takeaway_keeta = models.BooleanField(default=True)
    takeaway_foodpanda = models.BooleanField(default=True)
    is_published = models.BooleanField(default=True)
    discount_coupon = models.BooleanField(default=True)
    
    def __str__(self):
        return self.restaurant_name

# Create your models here.
