# Generated by Django 4.2.2 on 2023-06-29 05:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appweb', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Cargo',
            new_name='Especialidad',
        ),
        migrations.RenameField(
            model_name='profesional',
            old_name='cargo',
            new_name='Especialidad',
        ),
    ]
