from django.contrib import admin
from django.urls import path
from UsuarioApp.views import *
from UsuarioApp.forms import *

urlpatterns = [

    path('accounts/signup/', UserRegisterView.as_view(), name = 'sign up'),
    path('accounts/login/', UserLoginView.as_view(), name='login'),
    path('accounts/logout/', UserLogoutView.as_view(), name='logout'),
    path('accounts/edituser/', user_edit, name= 'edit user'),
    path('accounts/profile/', perfil_user_main, name= 'perfil user main'),
    path('accounts/profile/<usuario>', perfi_user, name= 'perfil user'),
]