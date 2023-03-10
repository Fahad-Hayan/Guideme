from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
# from django.contrib.auth.models import AbstractUser

# Create your models here.


# class User(AbstractUser):
#     firstname = AbstractUser.first_name
#     lastname = AbstractUser.last_name
#     password = AbstractUser.password
#     email = AbstractUser.email

def validate_min_length(value):
    if len(value) < 40:
        raise ValidationError(_('Field must have a minimum length of 30 characters.'))

def validate_max_length(value):
    if len(value) > 2000:
        raise ValidationError(_('Field must have a maximum length of 2000 characters.'))

class Country(models.Model):
    # catigories =[
    #         ('not specified','not specified'),
    #         ('Leisure','Leisure'),
    #         ('Archaeological','Archaeological'),
    #         ('Religious','Religious'),
    #         ],
    name = models.CharField(max_length=16, verbose_name='Country Name')
    image = models.ImageField(upload_to='images/%y/%m/%d', default='images/default/defaultImage.jpg', verbose_name='Photo')
    # cities = models.ForeignKey(City, on_delete= models.CASCADE)
    activeState = models.BooleanField(default=True, verbose_name='Active State')
    # city = models.JSONField(verbose_name='City',default= {
    #     'name':'',
    #     'country': models.ForeignKey(Country, on_delete=models.CASCADE, null= True)
    #     'caption': '',
    #     'image': '',
    #     'exchangeRate': '',
    #     'rating': '',
    #     'activeState': '',
    #     'catigory': '',
    #     },
    #     )
    class Meta:
        verbose_name = 'Country'
        verbose_name_plural = 'Countries'
        ordering = ['name']

    def __str__(self):
        return self.name

class City(models.Model):
    categories=[
        ('Not Specified', 'Not Specified'),
        ('Leisure Tourism','Leisure Tourism'),
        ('Archaeological Tourism','Archaeological Tourism'),
        ('Religious Tourism','Religious Tourism'),
    ]
    name = models.CharField(max_length=25, verbose_name= 'City Name')
    country = models.ForeignKey(Country, on_delete=models.CASCADE, null= True)
    caption = models.TextField(null = True, blank = False, verbose_name='Caption', validators=[validate_min_length,validate_max_length])
    image = models.ImageField(upload_to='images/%y/%m/%d', default='images/default/defaultImage.jpg', verbose_name='Image')
    exchangeRate = models.DecimalField(max_digits=6,decimal_places=2, verbose_name='Exchage Rate')
    rating = models.DecimalField(max_digits=2,decimal_places=1, verbose_name='Rating')
    activeState = models.BooleanField(default=True, verbose_name='Active State')
    category = models.CharField(max_length= 22, choices= categories, null=True, blank=True)
    class Meta:
        verbose_name = 'City'
        verbose_name_plural = 'Cities'
        ordering = ['-rating'] 
        
    def __str__(self):
        return self.name