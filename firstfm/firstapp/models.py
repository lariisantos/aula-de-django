from django.db import models

# Create your models here.
class Cantor(models.Model):
    nome = models.CharField(max_length=200)

class Album(models.Model):
    titulo = models.CharField(max_length=200)
    artista = models.TextField()
    genero = models.CharField(max_length=20)
    cantor = models.ForeignKey(Cantor, on_delete=models.CASCADE, null=True)
    ano_lancamento = models.SmallIntegerField(null=True)

class Musica(models.Model):
    titulo = models.CharField(max_length=200, null=False)
    compositor = models.TextField()
    duracao = models.CharField(max_length=5, null=False)
    album = models.ForeignKey(Album, on_delete=models.CASCADE)

class avaliacao_musica(models.Model):
    username =models.CharField(max_length=50, null=False)
    musica = models.ForeignKey(Musica, on_delete=models.CASCADE)
    nota = models.SmallIntegerField()