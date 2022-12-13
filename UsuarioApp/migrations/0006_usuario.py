# Generated by Django 4.1.3 on 2022-12-10 15:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UsuarioApp', '0005_userprofile_delete_usuario'),
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('password1', models.CharField(max_length=50)),
                ('password2', models.CharField(max_length=50)),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
            ],
        ),
    ]
