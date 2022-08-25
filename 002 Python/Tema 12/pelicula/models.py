from django.db import models
from django.urls import reverse

class Director(models.Model):
    name = models.CharField(max_length=34,help_text="Nombre del director")
    fotoURL = models.URLField()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('director-detail', args=[str(self.id)])

class Pelicula(models.Model):
    director = models.ForeignKey('Director', on_delete=models.CASCADE)
    name = models.CharField(max_length=64, help_text="Nombre de la pelicula")
    sumary = models.TextField(max_length=150, help_text="Descripcion de la pelicula")
    portadaURL = models.URLField()

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('pelicula-detail', args=[str(self.id)])