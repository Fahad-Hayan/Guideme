from django.shortcuts import render
from .models import Country, City
from django.http import HttpResponse
# Create your views here.

def home(request):
    return render(request, 'pages/home.html',{
        'cities' : City.objects.all().exclude(catigory='Not Specified'),
        'catigories': [
        'Most Rated',
        'Leisure Tourism',
        'Archaeological Tourism',
        'Religious Tourism',
    ],
    })

def destinations(request):
    return render(request, 'pages/destinations.html')

def wishlist(request):
    return render(request, 'pages/wishlist.html')

def about(request):
    return render(request, 'pages/about.html')

def registration(request):
    return render(request, 'pages/registration.html')

def favoriteIconFunction(request):
    pass