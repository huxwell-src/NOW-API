# Generated by Django 4.2.3 on 2023-08-19 22:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="solicitud",
            name="fecha_devolucion",
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name="solicitud",
            name="fecha_entrega",
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name="solicitud",
            name="fecha_solicitud",
            field=models.DateField(),
        ),
    ]
