from django.db import models

# Create your models here.
class Album(models.Model):
    titulo = models.CharField(max_length=200)
    artista = models.TextField()
    genero = models.CharField(max_length=20)

class Musica(models.Model):
    titulo = models.CharField(max_length=200, null=False)
    compositor = models.TextField()
    duracao = models.SmallIntegerField() #small = poucos bits armazenados
    album = models.ForeignKey(Album, on_delete=models.CASCADE) #caso apague um album, todas as musicas serão apagadas

