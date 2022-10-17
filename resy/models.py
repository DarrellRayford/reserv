from sqlite3 import Date
from unicodedata import category
from django.db import models

# Create your models here.

class reservation(models.Model):
    name = models.CharField(max_length=50)
    number_of_people = models.IntegerField()
    phone = models.IntegerField()
    Date = models.IntegerField()
    time = models.IntegerField()




    # location = models.CharField(max_length=100)
    # title = models.CharField(max_length=100)
    # description = models.CharField(max_length=250)
    # image = models.ImageField(upload_to='resy/images')
    # url = models.URLField(blank=True)