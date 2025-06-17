from django.contrib import admin

# Register your models here.
from .models import two_dish_rice
from django.forms import NumberInput
from django.db import models
class two_dish_riceAdmin(admin.ModelAdmin):
    list_display = 'id', 'restaurant_name', 'is_published', 'edit_date', 'two_dish_price', 'three_dish_price','drink_price','soup_price'
    list_display_links = 'id', 'restaurant_name'
    list_filter = 'restaurant_district',
    list_editable = 'edit_date', 'is_published', 'two_dish_price', 'three_dish_price','drink_price','soup_price'
    search_fields = 'restaurant_name', 'restaurant_district'
    list_per_page = 25
    ordering = ['-id']
    prepopulated_fields = {'restaurant_name': ('restaurant_name',)}
    formfield_overrides = {
        models.IntegerField: {'widget': NumberInput (attrs= {'size': '10'})}}
    show_facets = admin.ShowFacets.ALWAYS
admin.site.register(two_dish_rice, two_dish_riceAdmin)


# Register your models here.
