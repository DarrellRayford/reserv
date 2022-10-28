from sqlite3 import Date
from unicodedata import category
from django.db import models
from django.contib.auth.models import User

# Create your models here.

class Reservation(models.Model):
    name = models.CharField(max_length=50)
    number_of_people = models.IntegerField()
    phone = models.IntegerField()
    Date = models.IntegerField()
    time = models.IntegerField()

class Review(models.Model):
    text = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    restaurant = models.ForeignKey(Reservation, on_delete=models.CASCADE)
    reservAgain = models.BooleanField()

    def __str__(self):
        return self.text




    # location = models.CharField(max_length=100)
    # title = models.CharField(max_length=100)
    # description = models.CharField(max_length=250)
    # image = models.ImageField(upload_to='resy/images')
    # url = models.URLField(blank=True)