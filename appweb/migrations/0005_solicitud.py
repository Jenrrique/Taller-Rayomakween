# Generated by Django 4.2.1 on 2023-06-29 15:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('appweb', '0004_contacto'),
    ]

    operations = [
        migrations.CreateModel(
            name='Solicitud',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('foto', models.ImageField(null=True, upload_to='profesional')),
                ('estado', models.IntegerField()),
                ('contacto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appweb.contacto')),
                ('profesional', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appweb.profesional')),
            ],
        ),
    ]
