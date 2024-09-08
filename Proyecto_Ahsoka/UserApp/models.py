from django.db import models

# Create your models here.
class user(models.Model):

    nombre_usuario = models.CharField(max_length=50)
    contraseña = models.CharField(max_length=50)
    correo_electronico = models.EmailField(unique=True)
    fecha_nacimiento = models.DateField()
    foto_perfil = models.ImageField(upload_to='perfil_fotos/')
    activo = models.BooleanField(default=True)
