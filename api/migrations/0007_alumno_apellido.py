# Generated by Django 4.2.3 on 2023-10-15 19:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0006_alter_profesor_contrasena"),
    ]

    operations = [
        migrations.AddField(
            model_name="alumno",
            name="apellido",
            field=models.CharField(default="", max_length=50),
        ),
    ]
