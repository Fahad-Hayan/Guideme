from django.shortcuts import render
from .models import Country, City
from django.http import HttpResponse
# Create your views here.

def home(request):
    return render(request, 'pages/home.html',{
        'cities' : City.objects.all().exclude(category='Not Specified')[:10],
        'categories': [
        'Most Rated',
        'Leisure Tourism',
        'Archaeological Tourism',
        'Religious Tourism',
    ],
    'Countries' : Country.objects.all()
    })

def categories(request):
    return render(request, 'pages/categories.html')

def wishlist(request):
    return render(request, 'pages/wishlist.html')

def about(request):
    return render(request, 'pages/about.html')

def registration(request):
    return render(request, 'pages/registration.html')

def favoriteIconFunction(request):
    pass