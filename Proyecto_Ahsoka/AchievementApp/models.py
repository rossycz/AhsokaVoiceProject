from django.db import models
from UserApp.models import user
#from django.db.models.functions import Random
#from LogroApp.models import logro

#logro_aleatorio = logro.objects.order_by(Random()).first()


# Create your models here.
class achievement(models.Model):

    # Definición de las categorías
    CATEGORIA_OPCIONES = [
        ('academic', 'Académico'),
        ('professional', 'Profesional'),
        ('sport', 'Deportivo'),
        ('cultural', 'Cultural y Artístico'),
        ('community', 'Social y Comunitario'),
        ('tech', 'Tecnológico'),
        ('personal', 'Personal'),
        ('entrepreneurship', 'Emprendimiento'),
        ('financial', 'Financiero'),
        ('environmental', 'Medioambiental'),
        ('continuing_education', 'Educación Continua'),
    ]
    
    User=models.ForeignKey(user,null=True,blank=True,on_delete=models.CASCADE)
    titulo = models.CharField(max_length=200)
    # Campo de selección de categoría
    categoria = models.CharField(
        max_length=80,
        choices=CATEGORIA_OPCIONES,
        default='academic',
    )
    descripcion = models.TextField()
    fecha = models.DateField()
    imglogro = models.ImageField(upload_to="logros", null=True)
    status = models.BooleanField(default=True)

    class Meta:
        db_table = 'logro'
