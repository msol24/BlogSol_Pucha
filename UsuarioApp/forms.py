from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserRegisterForm(UserCreationForm):
    
    username = forms.CharField(label="Username")
    email = forms.EmailField()
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Confirme contraseña", widget=forms.PasswordInput)
    first_name = forms.CharField(label="Nombre")
    last_name = forms.CharField(label="Apellido")

    class Meta:
        
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'first_name', 'last_name']
        help_text = {k: "" for k in fields}

class UserEditForm(UserCreationForm):

    username = forms.CharField(label="Modificar username")
    email = forms.EmailField(label="Modificar email")
    password1 = forms.CharField(label='Nueva contraseña', widget=forms.PasswordInput, required=False)
    password2 = forms.CharField(label='Confirme nueva contraseña', widget=forms.PasswordInput, required=False)
    first_name = forms.CharField(label="Modificar nombre", required=False)
    last_name = forms.CharField(label=" Modificar apellido", required=False)

    class Meta:
        
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'first_name', 'last_name']
        help_text = {k: "" for k in fields}

class AvatarForm(forms.Form):

    img = forms.ImageField()


class PerfilUserForm(forms.Form):

    email = forms.EmailField(required=False, label='Email')
    instagram = forms.URLField(required=False, label='Instagram')
    descripcion = forms.CharField(widget=forms.Textarea, label='Descripción', required=False)


