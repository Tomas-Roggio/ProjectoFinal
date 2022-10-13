from django.db import models

# Create your models here.
class autor(models.Model):
    
    class Meta:
        verbose_name_plural="Autores"

    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    profecion = models.CharField(max_length=30)


class articulo(models.Model):
    titulo = models.CharField(max_length=40)
    texto = models.CharField(max_length=1000)
    fecha = models.DateField(null=True)


class seccion(models.Model):
    class Meta:
        verbose_name_plural="Selecciones"

    nombre = models.CharField(max_length=30)