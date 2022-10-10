from django.db import models

# Create your models here.

location = models.CharField(max_length=100)
title = models.CharField(max_length=100)
description = models.CharField(max_length=250)
image = models.ImageField(upload_to='resy/images')
url = models.URLField(blank=True)