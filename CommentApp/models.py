from django.db import models
from UserApp.models import User
from AchivementApp.models import Achievement

# Create your models here.

class Comment(models.Model):
    content = models.TextField()
    date = models.DateField()

    achievement = models.ForeignKey(Achievement,null=True,blank=True,on_delete=models.CASCADE)
    user = models.ForeignKey(User,null=True,blank=True,on_delete=models.CASCADE)
