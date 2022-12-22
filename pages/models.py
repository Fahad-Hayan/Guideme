from django.db import models

# Create your models here.


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
    catigories=[
        ('Not Specified', 'Not Specified'),
        ('Leisure Tourism','Leisure Tourism'),
        ('Archaeological Tourism','Archaeological Tourism'),
        ('Religious Tourism','Religious Tourism'),
    ]
    name = models.CharField(max_length=20, verbose_name= 'City Name')
    country = models.ForeignKey(Country, on_delete=models.CASCADE, null= True)
    caption = models.TextField(null = True, blank = True, verbose_name='Caption')
    image = models.ImageField(upload_to='images/%y/%m/%d', default='images/default/defaultImage.jpg', verbose_name='Image')
    exchangeRate = models.DecimalField(max_digits=6,decimal_places=2, verbose_name='Exchage Rate')
    rating = models.DecimalField(max_digits=2,decimal_places=1, verbose_name='Rating')
    activeState = models.BooleanField(default=True, verbose_name='Active State')
    catigory = models.CharField(max_length= 22, choices= catigories, null=True, blank=True)
    class Meta:
        verbose_name = 'City'
        verbose_name_plural = 'Cities'
        ordering = ['-rating'] 
        
    def __str__(self):
        return self.name