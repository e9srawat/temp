from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(AbstractUser):
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=15)
    

class Contact(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    name = models.CharField(max_length=25)
    mobile_number1 = models.CharField(max_length=10)
    mobile_number2 = models.CharField(max_length=10)
    email1 = models.EmailField()
    email2 = models.EmailField()
    address = models.CharField(max_length=100)
    age = models.CharField(max_length=3)
    ig = models.CharField(max_length=25)
    x = models.CharField(max_length=25)
    telegram = models.CharField(max_length=25)
    linkedin = models.CharField(max_length=25)
