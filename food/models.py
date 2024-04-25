from django.db import models
from django import forms
from django.contrib.auth.models import User
# Create your models here.

class FoodItem(models.Model):
    user_name = models.ForeignKey(User,on_delete=models.CASCADE,default=1)
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.IntegerField()
    image = models.CharField(max_length=500, blank=True,)

    def __str__(self) -> str:
        return self.name
    
class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    image = models.ImageField(default='profile.png', upload_to='images/')
    location = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.user.username
