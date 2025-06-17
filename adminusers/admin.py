from django.contrib import admin

from .models import Adminuser

# Register your models here.

class AdminuserAdmin(admin.ModelAdmin):
    list_display = ('id', 'admin_name', 'admin_email', 'admin_desc', 'admin_photo')
    list_display_links = ('id', 'admin_name')
    list_editable = ('admin_email', 'admin_desc', 'admin_photo')   
    search_fields = ('admin_name',)
    list_per_page = 25

admin.site.register(Adminuser, AdminuserAdmin)