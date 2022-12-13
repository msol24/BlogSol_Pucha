from django.db import models
from datetime import date, datetime
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
# Create your models here.

class Post(models.Model):

    usuario = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    fecha = models.DateField(auto_now_add=True)
    titulo = models.CharField(primary_key=True, max_length=50)
    subtitulo = models.CharField(max_length=100)
    imagen = models.ImageField(upload_to='imagenesposts', blank=True, null=True)
    cuerpo = RichTextField()
    
    def __str__(self):
        return f'{self.titulo} de {self.usuario}'

class Comentario(models.Model):

    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='post_comment_author')
    comentario = models.TextField()
    post = models.CharField(max_length=100, blank=True, null=True)
    fecha = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f'{self.usuario} | Comentario | {self.post}'