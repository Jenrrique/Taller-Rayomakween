# Generated by Django 4.2.1 on 2023-07-12 04:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appweb', '0013_postular'),
    ]

    operations = [
        migrations.CreateModel(
            name='Trabajo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('costo', models.CharField(max_length=100)),
                ('categoria', models.IntegerField(choices=[[0, 'Cambio de neumáticos'], [1, 'Cambio de aceite'], [2, 'Abolladura'], [3, 'Revisión de batería'], [4, 'Cambio de batería'], [5, 'Revisión de niveles'], [6, 'Caja de cambio'], [7, 'Cambio de pastillas de freno'], [8, 'Limpieza']])),
                ('foto', models.ImageField(null=True, upload_to='trabajo')),
                ('descripcion', models.TextField()),
            ],
        ),
    ]
