# Generated by Django 4.1.3 on 2022-12-10 20:49

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('UsuarioApp', '0006_usuario'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='UserProfile',
            new_name='PerfilUser',
        ),
        migrations.DeleteModel(
            name='Usuario',
        ),
    ]
