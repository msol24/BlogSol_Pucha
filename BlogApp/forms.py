from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from ckeditor.fields import RichTextField
from BlogApp.models import *

class PostCreateForm(forms.ModelForm):

    usuario = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    titulo = forms.CharField(label= 'Titulo del disco', max_length=50)
    subtitulo = forms.CharField(label= 'Banda', max_length=100)
    slug = models.CharField('Subgénero', max_length=50, blank=True, null=True)
    imagen = forms.ImageField(label='Foto')
    cuerpo = RichTextField()

    class Meta:
        model = Post
        fields = '__all__'
        help_text = {k: "" for k in fields}

class ComentarioCreateForm(forms.Form):

    usuario = forms.CharField(max_length=50)
    comentario = forms.CharField(widget=forms.Textarea)
    post = models.CharField(max_length=50)