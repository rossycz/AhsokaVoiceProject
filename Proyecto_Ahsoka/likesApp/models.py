from django.db import models
from UserApp.models import user
from AchievementApp.models import achievement
# Create your models here.
class Likes(models.Model):

    fecha=models.DateField()
    Achivement=models.ForeignKey(achievement,null=True,blank=True,on_delete=models.CASCADE)
    User=models.ForeignKey(user,null=True,blank=True,on_delete=models.CASCADE)
    
    class Meta:
        db_table = 'likes'
        