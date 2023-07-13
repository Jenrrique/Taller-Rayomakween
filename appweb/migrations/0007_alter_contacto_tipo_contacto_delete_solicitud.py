# Generated by Django 4.2.1 on 2023-06-29 16:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appweb', '0006_solicitud_fecha'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contacto',
            name='tipo_contacto',
            field=models.IntegerField(choices=[[0, 'Sugerencia'], [1, 'Reclamo'], [2, 'Felicitaciones']]),
        ),
        migrations.DeleteModel(
            name='Solicitud',
        ),
    ]