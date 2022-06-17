# Generated by Django 3.2.9 on 2022-06-13 06:10

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Director',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('primer_nombre', models.CharField(max_length=100)),
                ('primer_apellido', models.CharField(max_length=100)),
                ('segundo_apellido', models.CharField(max_length=100)),
                ('fecha_de_nacimiento', models.DateField(blank=True, null=True)),
                ('fecha_de_muerte', models.DateField(blank=True, null=True, verbose_name='Muerto')),
            ],
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Coloca aquí el genero de la pelicula', max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='Movies',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(help_text='Coloca aquí el titulo de la pelicula', max_length=32)),
                ('anio', models.CharField(help_text='Coloca aquí el año de la pelicula', max_length=4)),
                ('clasificacion', models.CharField(help_text='Coloca aqui la clasificación', max_length=10)),
                ('director', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalog.director')),
                ('genero', models.ManyToManyField(to='catalog.Genre')),
            ],
        ),
        migrations.CreateModel(
            name='MovieInstance',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, help_text='ID unico para la pelicula', primary_key=True, serialize=False)),
                ('imprimir', models.CharField(max_length=200)),
                ('due_back', models.DateField(blank=True, null=True)),
                ('status', models.CharField(blank=True, choices=[('p', 'Prestada'), ('d', 'Disponible'), ('m', 'Mantenimiento'), ('r', 'Reservada')], default='d', help_text='Estado de la pelicula', max_length=1)),
                ('movie', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalog.movies')),
            ],
        ),
    ]
