# Generated by Django 5.0.7 on 2024-08-07 22:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_usuario', models.CharField(max_length=50)),
                ('contraseña', models.CharField(max_length=50)),
                ('correo_electronico', models.EmailField(max_length=254, unique=True)),
                ('fecha_nacimiento', models.DateField()),
                ('foto_perfil', models.ImageField(upload_to='perfil_fotos/')),
                ('activo', models.BooleanField(default=True)),
            ],
        ),
    ]
