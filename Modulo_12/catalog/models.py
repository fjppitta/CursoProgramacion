#from audioop import reverse
from email.policy import default
from django.db import models
import uuid
from django.urls import reverse

# Create your models here.

class Genre(models.Model):
    name=models.CharField(max_length=64,help_text="Coloca aquí el genero de la pelicula")

    def __str__(self):
        return self.name

class Movie(models.Model):
    titulo = models.CharField(max_length=32,help_text='Coloca aquí el titulo de la pelicula')
    director = models.ForeignKey('Director',on_delete=models.SET_NULL,null=True)
    anio = models.CharField('Año',max_length=4,help_text='Coloca aquí el año de la pelicula')
    clasificacion = models.CharField(max_length=10,help_text='Coloca aqui la clasificación')
    genero = models.ManyToManyField(Genre)
    resumen = models.TextField(max_length=400,help_text='Coloca aqui un resumen de la pelicula',null=True)

    def __str__(self):
        return self.titulo

    def get_absolute_url(self):
        return reverse('movie-detail',args=[str(self.id)])

    def display_genre(self):
        return ', '.join([ genre.name for genre in self.genre.all()[:3] ])
    display_genre.short_description = 'Genero'

    class Meta:
        ordering = ['titulo']

class MovieInstance(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text="ID unico para la pelicula")
    movie = models.ForeignKey('Movie',on_delete=models.SET_NULL,null=True)
    productora = models.CharField(max_length=200)
    due_back = models.DateField(null=True,blank=True)

    LOAN_STATUS = (
        ('p','Prestada'),
        ('d','Disponible'),
        ('m','Mantenimiento'),
        ('r','Reservada'),
    )

    status = models.CharField(max_length=1, choices=LOAN_STATUS, blank=True, default='d', help_text="Estado de la pelicula")

    class Meta:
        ordering = ["due_back"]

    def __str__ (self):
        return '%s (%s)' % (self.id,self.movie.titulo)

class Director(models.Model):
    primer_nombre = models.CharField('Nombre',max_length=100)
    primer_apellido = models.CharField('Apellido',max_length=100)
    fecha_de_nacimiento = models.DateField(null=True,blank=True)
    fecha_de_muerte = models.DateField('Fecha de Fallecimiento',null=True,blank=True)

    def get_absolute_url(self):
        return reverse('director-detail',args=[str(self.id)])
    
    def __str__(self):
        return '%s, %s' % (self.primer_apellido,self.primer_nombre)
    
    class Meta:
        ordering = ['primer_apellido']
