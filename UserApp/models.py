from django.db import models

# Create your models here.

class User(models.Model):
    user_name = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    birthdate = models.DateField()
    profile_photo = models.ImageField(upload_to='profile_photos/',null=True)
    IsActive = models.BooleanField(default=True)