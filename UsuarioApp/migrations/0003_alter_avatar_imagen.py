# Generated by Django 4.1.3 on 2022-12-09 11:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UsuarioApp', '0002_avatar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='avatar',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='media/images/'),
        ),
    ]
