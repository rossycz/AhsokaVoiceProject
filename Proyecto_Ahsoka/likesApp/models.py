from django.db import models
from UsuarioApp.models import usuario
from LogroApp.models import logro
# Create your models here.
class Likes(models.Model):

    fecha=models.DateField()
    Achivement=models.ForeignKey(logro,null=True,blank=True,on_delete=models.CASCADE)
    User=models.ForeignKey(usuario,null=True,blank=True,on_delete=models.CASCADE)
    
    class Meta:
        db_table = 'likes'
        