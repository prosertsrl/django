# Generated by Django 4.2.9 on 2024-01-19 02:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('departamento', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='departamento',
            name='short_name',
            field=models.CharField(blank=True, max_length=20, unique=True, verbose_name='Nombre Corto'),
        ),
    ]
