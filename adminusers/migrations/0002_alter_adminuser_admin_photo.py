# Generated by Django 5.2.3 on 2025-06-18 05:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminusers', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='adminuser',
            name='admin_photo',
            field=models.ImageField(blank=True, null=True, upload_to='Admin_Photo/'),
        ),
    ]
