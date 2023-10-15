# Generated by Django 4.2.3 on 2023-10-15 22:36

import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ("auth", "0012_alter_user_first_name_max_length"),
        ("api", "0011_alter_alumno_contrasena"),
    ]

    operations = [
        migrations.CreateModel(
            name="CustomUser",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("password", models.CharField(max_length=128, verbose_name="password")),
                (
                    "last_login",
                    models.DateTimeField(
                        blank=True, null=True, verbose_name="last login"
                    ),
                ),
                (
                    "is_superuser",
                    models.BooleanField(
                        default=False,
                        help_text="Designates that this user has all permissions without explicitly assigning them.",
                        verbose_name="superuser status",
                    ),
                ),
                (
                    "username",
                    models.CharField(
                        error_messages={
                            "unique": "A user with that username already exists."
                        },
                        help_text="Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.",
                        max_length=150,
                        unique=True,
                        validators=[
                            django.contrib.auth.validators.UnicodeUsernameValidator()
                        ],
                        verbose_name="username",
                    ),
                ),
                (
                    "first_name",
                    models.CharField(
                        blank=True, max_length=150, verbose_name="first name"
                    ),
                ),
                (
                    "last_name",
                    models.CharField(
                        blank=True, max_length=150, verbose_name="last name"
                    ),
                ),
                (
                    "email",
                    models.EmailField(
                        blank=True, max_length=254, verbose_name="email address"
                    ),
                ),
                (
                    "is_staff",
                    models.BooleanField(
                        default=False,
                        help_text="Designates whether the user can log into this admin site.",
                        verbose_name="staff status",
                    ),
                ),
                (
                    "is_active",
                    models.BooleanField(
                        default=True,
                        help_text="Designates whether this user should be treated as active. Unselect this instead of deleting accounts.",
                        verbose_name="active",
                    ),
                ),
                (
                    "date_joined",
                    models.DateTimeField(
                        default=django.utils.timezone.now, verbose_name="date joined"
                    ),
                ),
                (
                    "rol",
                    models.CharField(
                        choices=[
                            ("alumno", "Alumno"),
                            ("profesor", "Profesor"),
                            ("administrador", "Administrador"),
                            ("bodeguero", "Bodeguero"),
                        ],
                        max_length=15,
                    ),
                ),
                (
                    "groups",
                    models.ManyToManyField(
                        blank=True,
                        related_name="customuser_set",
                        related_query_name="user",
                        to="auth.group",
                    ),
                ),
                (
                    "user_permissions",
                    models.ManyToManyField(
                        blank=True,
                        related_name="customuser_set",
                        related_query_name="user",
                        to="auth.permission",
                    ),
                ),
            ],
            options={
                "verbose_name": "user",
                "verbose_name_plural": "users",
                "abstract": False,
            },
            managers=[
                ("objects", django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.AddField(
            model_name="administrador",
            name="user",
            field=models.OneToOneField(
                default=None,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="api.customuser",
            ),
        ),
        migrations.AddField(
            model_name="alumno",
            name="user",
            field=models.OneToOneField(
                default="administrador",
                on_delete=django.db.models.deletion.CASCADE,
                to="api.customuser",
            ),
        ),
        migrations.AddField(
            model_name="bodeguero",
            name="user",
            field=models.OneToOneField(
                default="bodeguero",
                on_delete=django.db.models.deletion.CASCADE,
                to="api.customuser",
            ),
        ),
        migrations.AddField(
            model_name="profesor",
            name="user",
            field=models.OneToOneField(
                default="profesor",
                on_delete=django.db.models.deletion.CASCADE,
                to="api.customuser",
            ),
        ),
    ]