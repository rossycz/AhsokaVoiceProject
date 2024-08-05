from django.db import models

# Create your models here.
class logro(models.Model):
    
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField(max_length=100)
    fecha = models.DateField()
    imglogro = models.ImageField(upload_to="logros", null=True)
