from django.db import models
from django.core.exceptions import ValidationError

class Showroomlist(models.Model):
    name = models.CharField(max_length=50)
    location = models.CharField(max_length=200)
    website = models.URLField(max_length=100)
    
    def __str__(self):
        return self.name

class Carlist(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    active = models.BooleanField(default=False)
    chassisnumber = models.CharField(max_length=100,blank=True,null=True)
    price = models.DecimalField(max_digits=10,decimal_places=2,blank=True,null=True)
    
    def __str__(self):
        return self.name