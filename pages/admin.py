from django.contrib import admin
from .models import Country, City
# Register your models here.

admin.site.register(Country)
admin.site.register(City)

admin.site.site_header = 'Guideme Admin Panel'
admin.site.site_title = 'Guideme Admin Panel'