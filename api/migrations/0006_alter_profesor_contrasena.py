# Generated by Django 4.2.3 on 2023-10-15 18:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0005_herramienta_lvl_stock"),
    ]

    operations = [
        migrations.AlterField(
            model_name="profesor",
            name="contrasena",
            field=models.CharField(blank=True, default="", max_length=255),
        ),
    ]
