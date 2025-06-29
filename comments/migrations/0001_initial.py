# Generated by Django 5.2.2 on 2025-06-16 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='comment_rate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('two_dish_rice_id', models.IntegerField()),
                ('foodie_name_id', models.IntegerField()),
                ('restaurant_name', models.CharField(max_length=200)),
                ('foodie_name', models.CharField(max_length=200)),
                ('list_date', models.DateTimeField(auto_now_add=True)),
                ('edit_date', models.DateField(blank=True)),
                ('comment', models.TextField(blank=True)),
                ('comment_photo1', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/')),
                ('comment_photo2', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/')),
                ('comment_photo3', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/')),
                ('comment_photo4', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/')),
                ('comment_photo5', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/')),
                ('comment_photo6', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/')),
                ('is_published', models.BooleanField(default=True)),
                ('restaurant_rating', models.IntegerField(blank=True, null=True)),
                ('comment_rating', models.IntegerField(blank=True, null=True)),
            ],
        ),
    ]
