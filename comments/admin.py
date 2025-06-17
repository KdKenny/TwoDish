from django.contrib import admin

# Register your models here.
from .models import comment_rate
from django.forms import NumberInput
from django.db import models
class comment_rate_Admin(admin.ModelAdmin):
    list_display = 'id', 'restaurant_name', 'foodie_name', 'is_published', 'edit_date'
    list_display_links = 'id', 'restaurant_name', 'foodie_name'
    list_filter = 'restaurant_name', 'foodie_name', 
    list_editable = 'edit_date', 'is_published',
    search_fields = 'restaurant_name', 'foodie_name'
    list_per_page = 25
    ordering = ['-id']
    prepopulated_fields = {'foodie_name': ('foodie_name',)}
    formfield_overrides = {
        models.IntegerField: {'widget': NumberInput (attrs= {'size': '10'})}}
    show_facets = admin.ShowFacets.ALWAYS
admin.site.register(comment_rate, comment_rate_Admin)


# Register your models here.