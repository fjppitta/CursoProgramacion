# Generated by Django 3.2.9 on 2022-06-13 21:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0004_remove_director_segundo_apellido'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='movieinstance',
            options={'ordering': ['due_back']},
        ),
        migrations.RenameField(
            model_name='movieinstance',
            old_name='imprimir',
            new_name='productora',
        ),
    ]