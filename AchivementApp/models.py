from django.db import models

# Create your models here.
class Achievement(models.Model):
    #Listado de categorías
    CATEGORY_OPTIONS = [
        ('Académico','Academic'),
        ('Profesional','Professional'),
        ('Deportivo','Sport'),
         ('Cultural y Artístico','Cultural_and_Artistic'),
        ('Social y Comunitario','Social_and_Community'),
        ('Tecnológico','Tech'),
        ('Personal', 'Personal'),
        ('Emprendimiento','Entrepreneurship'),
        ('Financiero','Financial'),
        ('Medioambiental','Environmental'),
        ('Educación Continua', 'Continuing_Education'),

    ]


    title = models.CharField(max_length=200)
    category = models.CharField(max_length=80,
                                choices=CATEGORY_OPTIONS,
                                default='Academic')
    description = models.TextField()
    date = models.DateField()
    achievement_image = models.ImageField(upload_to="achievements_img",null=True)  
    status = models.BooleanField(default=True)

