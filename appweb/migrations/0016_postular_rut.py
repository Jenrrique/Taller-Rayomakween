# Generated by Django 4.2.1 on 2023-07-13 03:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appweb', '0015_alter_profesional_fecha_nacimiento_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='postular',
            name='rut',
            field=models.CharField(max_length=10, null=True),
        ),
    ]
