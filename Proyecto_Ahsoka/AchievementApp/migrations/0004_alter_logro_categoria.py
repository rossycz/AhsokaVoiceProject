# Generated by Django 5.0.7 on 2024-08-10 07:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LogroApp', '0003_alter_logro_descripcion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='logro',
            name='categoria',
            field=models.CharField(choices=[('academic', 'Académico'), ('professional', 'Profesional'), ('sport', 'Deportivo'), ('cultural', 'Cultural y Artístico'), ('community', 'Social y Comunitario'), ('tech', 'Tecnológico'), ('personal', 'Personal'), ('entrepreneurship', 'Emprendimiento'), ('financial', 'Financiero'), ('environmental', 'Medioambiental'), ('continuing_education', 'Educación Continua')], default='academic', max_length=80),
        ),
    ]
