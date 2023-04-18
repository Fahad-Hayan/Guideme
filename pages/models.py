from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User

# Create your models here.


# class User(AbstractUser):
#     firstname = AbstractUser.first_name
#     lastname = AbstractUser.last_name
#     password = AbstractUser.password
#     email = AbstractUser.email
#     user_permissions = AbstractUser.user_permissions
#     groups = AbstractUser.groups

def validate_min_length(value):
    if len(value) < 40:
        raise ValidationError(_('Field must have a minimum length of 40 characters.'))

def validate_max_length(value):
    if len(value) > 2000:
        raise ValidationError(_('Field must have a maximum length of 2000 characters.'))


class Country(models.Model):
    name = models.CharField(max_length=16, verbose_name='Country Name', unique= True)
    image = models.ImageField(upload_to='images/%y/%m/%d', default='images/default/defaultImage.jpg', verbose_name='Photo')
    activeState = models.BooleanField(default=True, verbose_name='Active State')
    class Meta:
        verbose_name = 'Country'
        verbose_name_plural = 'Countries'
        ordering = ['name']

    def __str__(self):
        return self.name

class Category(models.Model):
    type = models.CharField(max_length= 22, null=True, blank=True, unique=True)
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
    def __str__(self):
        return self.type

class Activity(models.Model):
    title = models.CharField(max_length=50, unique=True)
    type = models.ForeignKey(Category, to_field='type', db_constraint=False, on_delete= models.CASCADE, null=True)
    caption = models.TextField(blank=True, unique=True)
    cityName = models.CharField(max_length=25, verbose_name= 'City Name', default='all')
    image = models.ImageField(upload_to='images/%y/%m/%d', default='images/default/defaultImage.jpg', verbose_name='Image')
    class Meta:
        verbose_name = 'Activity'
        verbose_name_plural = 'Activities'
        ordering = ['cityName','type','title']
    def __str__(self):
        return ('(' + self.cityName + ' - ' + str(self.type) +'): '+ self.title)

class Restaurants(models.Model):
    R_name = models.CharField(max_length=50, unique=True, verbose_name='Name')
    caption = models.TextField(blank=True, unique=True)
    cityName = models.CharField(max_length=25, verbose_name= 'City Name', default='all')
    image = models.ImageField(upload_to='images/%y/%m/%d', default='images/default/defaultImage.jpg', verbose_name='Image')
    class Meta:
        verbose_name = 'Restaurant'
        verbose_name_plural = 'Restaurants'
        ordering = ['cityName','R_name']
    def __str__(self):
        return ('(' +self.cityName +'): '+self.R_name)

class Hotels(models.Model):
    H_name = models.CharField(max_length=50, unique=True, verbose_name='Name')
    caption = models.TextField(blank=True, unique=True)
    cityName = models.CharField(max_length=25, verbose_name= 'City Name', default='all')
    image = models.ImageField(upload_to='images/%y/%m/%d', default='images/default/defaultImage.jpg', verbose_name='Image')
    class Meta:
        verbose_name = 'Hotel'
        verbose_name_plural = 'Hotels'
        ordering = ['cityName','H_name']
    def __str__(self):
        return ('(' + self.cityName +'): '+self.H_name)
class City(models.Model):
    name = models.CharField(max_length=25, verbose_name= 'City Name')
    country = models.ForeignKey(Country, on_delete=models.CASCADE, null= True, to_field='name', db_constraint=False)
    caption = models.TextField(null = True, blank = False, verbose_name='Caption', validators=[validate_min_length,validate_max_length], help_text='Caption length must be between 40 and 2000 characters')
    image = models.ImageField(upload_to='images/%y/%m/%d', default='images/default/defaultImage.jpg', verbose_name='Image')
    exchangeRate = models.DecimalField(max_digits=6,decimal_places=2, verbose_name='Exchage Rate',help_text='The value of the local currency against one USD')
    rating = models.DecimalField(max_digits=2,decimal_places=1, verbose_name='Rating' ,max_length=5, help_text='Must be from 0 to 5')
    activeState = models.BooleanField(default=True, verbose_name='Active State')
    inWishlist = models.ManyToManyField(User, related_name='inWishList', blank=True)
    category = models.ForeignKey(Category, to_field='type', db_constraint=False, on_delete= models.CASCADE, null=True)
    mapSrc = models.TextField(verbose_name='Map Source', blank= True)
    activities = models.ManyToManyField(Activity, blank= True)
    restaurants = models.ManyToManyField(Restaurants, blank=True)
    hotels = models.ManyToManyField(Hotels, blank=True)
    class Meta:
        verbose_name = 'City'
        verbose_name_plural = 'Cities'
        ordering = ['-rating'] 
        
    def __str__(self):
        return (self.name + " - " + str(self.category))

class Wishlist(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    cities = models.ManyToManyField(City, blank=True)
    class Meta:
        verbose_name = 'Wish List'
        verbose_name_plural = 'Wish Lists'
    
    def __str__(self):
        return str(self.user)

