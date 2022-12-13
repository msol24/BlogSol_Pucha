# Generated by Django 4.1.3 on 2022-12-06 07:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comentario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('usuario', models.CharField(max_length=50)),
                ('fecha', models.DateTimeField(auto_now_add=True)),
                ('cuerpo', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('usuario', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('fecha', models.DateField(auto_now_add=True)),
                ('titulo', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('subtitulo', models.CharField(max_length=100)),
                ('imagen', models.ImageField(blank=True, null=True, upload_to='imagenesposts')),
                ('cuerpo', models.TextField(verbose_name='')),
            ],
        ),
    ]
