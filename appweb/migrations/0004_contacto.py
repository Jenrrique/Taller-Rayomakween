# Generated by Django 4.2.1 on 2023-06-29 06:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appweb', '0003_rename_especialidad_profesional_especialidad_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contacto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=150)),
                ('telefono', models.IntegerField()),
                ('tipo_contacto', models.IntegerField(choices=[[0, 'Sugerencia'], [1, 'Reclamo'], [2, 'Felicitaciones'], [3, 'Solicitud']])),
                ('mensaje', models.TextField()),
            ],
        ),
    ]
