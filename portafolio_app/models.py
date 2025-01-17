from django.db import models

# Create your models here.
#Representa una tabla de la base de datos
class proyecto(models.Model):
    # los atributos verbose_name son para el panel de administración del proyecto
    titulo = models.CharField(max_length=200, verbose_name = "Titulo de película")
    descripcion = models.TextField(verbose_name = "Descripcion de la película")
    imagen = models.ImageField(verbose_name = "Imagen de película", upload_to="proyectos")
    url = models.URLField(verbose_name="Enlace de la película", null=True, blank=True)
    #Se ejecuta cuando se crea
    fecha_creacion = models.DateTimeField(auto_now_add=True, verbose_name = "Fecha de creación")
    #Se ejecuta cada que que se crea una instancia
    fecha_modificacion = models.DateTimeField(auto_now=True, verbose_name = "Fecha de edicion")

    # clase metadatos para mostrar el nombre en plural
    class meta:
        verbose_name = "Peliculas"
        verbose_name_plural = "Peliculas"
        ordering = ["-created"]
    # metodo para mostrar el nombre del proyecto
    def __str__(self):
        return self.titulo