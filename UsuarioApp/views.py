from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from UsuarioApp.models import *
from UsuarioApp.forms import *

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin



class UserRegisterView(CreateView):
    form_class = UserRegisterForm
    success_url = reverse_lazy('login')
    template_name = 'UsuarioApp/signup.html'

class UserLoginView(LoginView):
    template_name = 'UsuarioApp/login.html'

class UserLogoutView(LogoutView):
    template_name = 'UsuarioApp/logout.html'


@login_required(login_url='login')
def user_edit(request):

    usuario = request.user
    
    if request.method == 'POST':
        usuario_form = UserEditForm(request.POST)

        if usuario_form.is_valid():
            info = usuario_form.cleaned_data
            usuario.email = info ['email']
            usuario.first_name = info ['first_name']
            usuario.last_name = info ['last_name']

            usuario.save()

            return render(request, 'BlogApp/home.html')

    else:
        usuario_form = UserEditForm(initial={
            'username': usuario.username,
            'email': usuario.email
        })
    return render(request, 'UsuarioApp/user_edit.html', {
        'form': usuario_form, 
        'usuario': usuario
    })

@login_required(login_url='login')
def perfi_user(request, usuario):

    user = User.objects.get(username=usuario)

    usuario1= user.id

    avatar = Avatar.objects.filter(user=usuario1)

    if len(avatar) > 0:

        imgprofile = avatar[0].imagen.url

    else:

        imgprofile = None

    aboutuser = PerfilUser.objects.filter(user=usuario1)

    if len(aboutuser) > 0:


        email = aboutuser[0].email
        instagram = aboutuser[0].instagram
        descripcion = aboutuser[0].descripcion

    else:

        email = None
        instagram = None
        descripcion = 'no disponible aún'


    if request.user.username:

        avatar1 = Avatar.objects.filter(user=request.user)

        if len(avatar1) > 0:

            img = avatar1[0].imagen.url

        else:

            img = None
    
    else:

        img = None

    return render(request, 'UsuarioApp/perfil_user.html', {'img': img, 'user': user, 'imgprofile': imgprofile, 'email':email, 'instagram':instagram, 'descripcion':descripcion})



@login_required(login_url='login')
def perfil_user_main(request):
    
    user = request.user

    avatar = Avatar.objects.filter(user=request.user)

    if len(avatar) > 0:

        imgprofile = avatar[0].imagen.url

    else:

        imgprofile = None

    aboutuser = PerfilUser.objects.filter(user=request.user)

    if len(aboutuser) > 0:

        email = aboutuser[0].email
        instagram = aboutuser[0].instagram
        descripcion = aboutuser[0].descripcion

    else:
    
        email = None
        instagram = None
        descripcion = 'no disponible aún'

    if request.user.username:

        avatar1 = Avatar.objects.filter(user=request.user)

        if len(avatar1) > 0:

            img = avatar1[0].imagen.url

        else:

            img = None
    
    else:

        img = None

    return render(request, 'UsuarioApp/perfil_user.html', {'img': img, 'user': user, 'imgprofile': imgprofile, 'email':email, 'instagram':instagram, 'descripcion':descripcion})
