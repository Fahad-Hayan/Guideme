from django.urls import path
from . import views

urlpatterns=[
    path('', views.home, name='home'),
    path('explore', views.explore, name='explore'),
    path('wishlist/', views.wishlist, name='wishlist'),
    path('about', views.about, name='about'),
    path('signup', views.signup, name='signup'),
    path('signin', views.signin, name='signin'),
    path('signout', views.signout, name='signout'),
    path('profile', views.profile, name='profile'),
    path('countries/<countryName>/<cityId>', views.details, name='details'),
    path('countries/<countryName>', views.countries, name='countries'),
    path('countries', views.countries, name='countries'),
    path('wishlist/<int:city_id>/', views.wishlist_add_remove, name='wishlist_add_remove'),

    # path('email_confirmation', views.email_confirmation, name='email_confirmation'),
    # path('activate/<uidb64>/<token>', views.activate, name='activate'),
]