# Generated by Django 5.2.2 on 2025-06-16 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='two_dish_rice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('restaurant_name', models.CharField(max_length=200)),
                ('list_date', models.DateTimeField(auto_now_add=True)),
                ('edit_date', models.DateField(blank=True)),
                ('restaurant_photo_main', models.ImageField(blank=True, upload_to='photos/')),
                ('restaurant_area', models.CharField(choices=[('Hong Kong', 'Hong Kong'), ('Kowloon', 'Kowloon'), ('New Territories', 'New Territories'), ('Island', 'Island')], max_length=50)),
                ('restaurant_district', models.CharField(choices=[('Islands', 'Islands'), ('Kwai Tsing', 'Kwai Tsing'), ('North', 'North'), ('Sai Kung', 'Sai Kung'), ('Sha Tin', 'Sha Tin'), ('Tai Po', 'Tai Po'), ('Tuen Mun', 'Tuen Mun'), ('Tsuen Wan', 'Tsuen Wan'), ('Yuen Long', 'Yuen Long'), ('Kowloon City', 'Kowloon City'), ('Kwun Tong', 'Kwun Tong'), ('Sham Shui Po', 'Shum Shui Po'), ('Wang Tai Sin', 'Wong Tai Sin'), ('Yau Tsim Mong', 'Yau Tsim Mong'), ('Central & Western', 'Central & Western'), ('Eastern', 'Eastern'), ('Southern', 'Southern'), ('Wan Chai', 'Wan Chai')], max_length=50)),
                ('restaurant_street', models.CharField(max_length=200)),
                ('restaurant_address', models.CharField(max_length=200)),
                ('fullday', models.BooleanField(default=True)),
                ('openhour_fullday', models.TimeField(blank=True, null=True)),
                ('closehour_fullday', models.TimeField(blank=True, null=True)),
                ('afternoon', models.BooleanField(default=True)),
                ('openhour_afternoon', models.TimeField(blank=True, null=True)),
                ('closehour_afternoon', models.TimeField(blank=True, null=True)),
                ('night', models.BooleanField(default=True)),
                ('openhour_night', models.TimeField(blank=True, null=True)),
                ('closehour_night', models.TimeField(blank=True, null=True)),
                ('nightsnack', models.BooleanField(default=True)),
                ('openhour_nightsnack', models.TimeField(blank=True, null=True)),
                ('closehour_nightsnack', models.TimeField(blank=True, null=True)),
                ('category_chinese', models.BooleanField(default=True)),
                ('category_western', models.BooleanField(default=True)),
                ('category_seafood', models.BooleanField(default=True)),
                ('category_veg', models.BooleanField(default=True)),
                ('category_japan', models.BooleanField(default=True)),
                ('menu', models.TextField(blank=True)),
                ('menu_photo1', models.ImageField(blank=True, upload_to='photos/')),
                ('menu_photo2', models.ImageField(blank=True, upload_to='photos/')),
                ('menu_photo3', models.ImageField(blank=True, upload_to='photos/')),
                ('menu_photo4', models.ImageField(blank=True, upload_to='photos/')),
                ('menu_photo5', models.ImageField(blank=True, upload_to='photos/')),
                ('menu_photo6', models.ImageField(blank=True, upload_to='photos/')),
                ('two_dish_price', models.IntegerField()),
                ('three_dish_price', models.IntegerField()),
                ('drink_price', models.IntegerField()),
                ('soup_price', models.IntegerField()),
                ('payment_cash', models.BooleanField(default=True)),
                ('payment_octopus', models.BooleanField(default=True)),
                ('payment_alipayhk', models.BooleanField(default=True)),
                ('payment_wechatpay', models.BooleanField(default=True)),
                ('payment_payeme', models.BooleanField(default=True)),
                ('dine_in', models.BooleanField(default=True)),
                ('takeaway', models.BooleanField(default=True)),
                ('takeaway_self', models.BooleanField(default=True)),
                ('takeaway_keeta', models.BooleanField(default=True)),
                ('takeaway_foodpanda', models.BooleanField(default=True)),
                ('is_published', models.BooleanField(default=True)),
                ('discount_coupon', models.BooleanField(default=True)),
            ],
        ),
    ]
