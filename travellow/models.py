from typing import ClassVar
from django.db import models

# Create your models here.

class Destination(models.Model):
    
    name =  models.CharField(max_length=20)
    desc = models.TextField()
    img = models.ImageField(upload_to="pix")
    price = models.IntegerField()
    offer = models.BooleanField(default=False)