from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import TemplateView, ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from BlogApp.models import *
from UsuarioApp.models import *
from BlogApp.forms import *

from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin


def home(request):

    if request.user.username:

        avatar = Avatar.objects.filter(user=request.user)

        usuario = request.user

        if len(avatar) > 0:

            img = avatar[0].imagen.url

        else:

            img = None

    else:

        img = None

        usuario = None

    return render(request, 'BlogApp/templates/BlogApp/home.html', {'user': usuario, 'img':img})

def about(request):
    return render(request, 'BlogApp/templates/BlogApp/aboutme.html')


def chat(request):
    return render(request, 'BlogApp/templates/BlogApp/chat.html')


class CrearPost(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostCreateForm
    template_name = 'BlogApp/crear_post.html'
    success_url = reverse_lazy('ver posts')
    login_url = reverse_lazy('login')
    
    def get_initial(self):
        return {'usuario_post':self.request.user,'email':self.request.user.email}

    def get_context_data(self, *args, **kwargs ):

        avatar = Avatar.objects.filter(user=self.request.user)

        if len(avatar) > 0:
            img = avatar[0].imagen.url

        else:
            img = None

        context = super(CrearPost, self).get_context_data(**kwargs)
        context['img']=img
        return context   
        

class VerPosts(ListView):
    model = Post
    context_object_name = 'posts'
    template_name = 'BlogApp/ver_posts.html'
    queryset = Post.objects.all().order_by('-fecha')
    fields = "__all__"

    def get_context_data(self, *args, **kwargs ):

        if self.request.user.username:
        
                avatar = Avatar.objects.filter(user=self.request.user)

                usuario = self.request.user

                if len(avatar) > 0:
                
                    img = avatar[0].imagen.url

                else:
                
                    img = None

        else:
        
            img = None
            usuario = None

        context = super(VerPosts, self).get_context_data(**kwargs)
        context['img']=img
        context['usuario']=usuario
        return context

class DetallePost(DetailView):

    model = Post
    template_name = "BlogApp/post.html"   
    fields= "__all__"     

    def get_context_data(self, *args, **kwargs ):
        pk = self.kwargs.get('pk')

        if self.request.user.username:
        
            avatar = Avatar.objects.filter(user=self.request.user)

            usuario = self.request.user

            if len(avatar) > 0:
                
                img = avatar[0].imagen.url

            else:
                
                img = None

        else:
        
            img = None
            usuario = None

        context = super(DetallePost, self).get_context_data(**kwargs)
        context = super(DetallePost, self).get_context_data(**kwargs)
        context['comentarios']=Comentario.objects.filter(post=pk)
        context['img']=img

        return context   


class EditarPost(LoginRequiredMixin, UpdateView):
    model = Post
    template_name = 'BlogApp/editar_post.html'
    form_class = PostCreateForm
    success_url = reverse_lazy('ver posts')

class EliminarPost(LoginRequiredMixin, DeleteView):
    model = Post
    success_url = reverse_lazy('ver posts')

@login_required(login_url='login')
def crear_comentario(request, titulo):

    avatar = Avatar.objects.filter(user=request.user)

    if len(avatar) > 0:
        img = avatar[0].imagen.url

    else:
        img = None

    if request.method =='POST':

        comentario = ComentarioCreateForm(request.POST)

        if comentario.is_valid():

            content = comentario.cleaned_data

            post = Post.objects.filter(titulo=titulo)

            post = post[0].titulo

            comment = Comentario(usuario=request.user, comentario=content['comentario'], post = post)

            comment.save()

            postslist = Post.objects.all().order_by('-fecha')

            return render(request, 'BlogApp/comentario_exitoso.html', {'postlist': postslist, 'img': img})
    
    else:

        post = Post.objects.filter(titulo=titulo)

        post = post[0].titulo

        comentario = ComentarioCreateForm(initial={'usuario':request.user, 'post':post})

    return render(request, 'BlogApp/crear_comentario.html', {'comentario': comentario, 'img': img})

@login_required(login_url='login')
def open_user_profile(request, usuario):

    user = User.objects.get(username=usuario)

    usuario1= user.id

    avatar = Avatar.objects.filter(user=usuario1)

    if len(avatar) > 0:

        imgprofile = avatar[0].imagen.url

    else:

        imgprofile = None

    aboutuser = UserAbout.objects.filter(user=usuario1)

    if len(aboutuser) > 0:

        bio = aboutuser[0].bio
        instagram = aboutuser[0].instagram
        facebook = aboutuser[0].facebook
        twitter = aboutuser[0].twitter

    else:
    
        bio = 'Información no disponible aún.'
        instagram = None
        facebook = None
        twitter = None

    if request.user.username:

        avatar1 = Avatar.objects.filter(user=request.user)

        if len(avatar1) > 0:

            img = avatar1[0].imagen.url

        else:

            img = None
    
    else:

        img = None

    return render(request, 'appUsers/profile.html', {'img': img, 'user': user, 'imgprofile': imgprofile, 'bio':bio, 'instagram':instagram, 'facebook':facebook, 'twitter':twitter})
