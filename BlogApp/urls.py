from django.contrib import admin
from django.urls import path
from BlogApp.views import *

urlpatterns = [
    path('', home, name='home'),
    path('about/', about, name='aboutme'),
    path('messages/', chat, name='chat'),
    path('crear_comentario/<titulo>', crear_comentario, name='comentario'),

    path('crear_post/', CrearPost.as_view(), name='crear post'),
    path('pages/', VerPosts.as_view(), name='ver posts'),
    path('detalle_post/<pk>', DetallePost.as_view(), name='detalle post'),   
    path('editar_post/<pk>', EditarPost.as_view(), name='editar post'),
    path('confirm_eliminar_post/<pk>', EliminarPost.as_view(), name='eliminar post'),


]