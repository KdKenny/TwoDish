from django.contrib import admin

# Register your models here.


from .models import Contact
from django.forms import NumberInput
from django.db import models

class content_foodie_admin(admin.ModelAdmin):
    list_display = 'id','foodie_name', 'gender', 'age_range', 'occupation', 'live_district', 'is_mvp'
    list_display_links = 'id',
    list_filter = 'foodie_name',
    list_editable = 'occupation', 'live_district', 'is_mvp'
    search_fields = 'foodie_name',
    list_per_page = 25
   ## ordering = ['-id']
    prepopulated_fields = {'foodie_name' : ('foodie_name',)}
    formfield_overrides = {
        models.IntegerField: {'widget' : NumberInput(attrs= {'size': '10'})}}
    show_facets = admin.ShowFacets.ALWAYS


admin.site.register(Contact, content_foodie_admin)


