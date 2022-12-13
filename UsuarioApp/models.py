from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Avatar(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='avatar', null=True, blank=True)

    def __str__(self):
        return f'{self.user} | Avatar'

class PerfilUser(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    email = models.EmailField()
    instagram = models.URLField()
    descripcion = models.TextField(max_length=100)

    def __str__(self):
        return f'{self.user} | Perfil'





