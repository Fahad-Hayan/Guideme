from django.urls import path
from . import views

urlpatterns=[
    path('home', views.home, name='home'),
    path('destinations', views.destinations, name='destinations'),
    path('wishlist', views.wishlist, name='wishlist'),
    path('about', views.about, name='about'),
    path('registration', views.registration, name='registration'),
]