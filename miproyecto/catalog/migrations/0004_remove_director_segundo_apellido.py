# Generated by Django 3.2.9 on 2022-06-13 18:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0003_movie_resumen'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='director',
            name='segundo_apellido',
        ),
    ]
