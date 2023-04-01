from django.contrib import admin
from .models import Country, City, Category, Activity, Restaurants, Hotels
# Register your models here.

admin.site.register(Country)
admin.site.register(City)
admin.site.register(Category)
admin.site.register(Activity)
admin.site.register(Restaurants)
admin.site.register(Hotels)

admin.site.site_header = 'Guideme Admin Panel'
admin.site.site_title = 'Guideme Admin Panel'