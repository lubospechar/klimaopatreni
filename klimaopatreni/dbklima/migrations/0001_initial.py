# Generated by Django 5.0.6 on 2024-06-19 11:11

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Localization",
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
                (
                    "localization_name",
                    models.CharField(
                        max_length=30, verbose_name="Pojmenování lokalizace"
                    ),
                ),
            ],
            options={
                "verbose_name": "Lokalizace",
                "verbose_name_plural": "Lokalizace",
            },
        ),
        migrations.CreateModel(
            name="Group",
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
                (
                    "group_name",
                    models.CharField(max_length=30, verbose_name="Pojmenování skupiny"),
                ),
                (
                    "localization",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="dbklima.localization",
                    ),
                ),
            ],
            options={
                "verbose_name": "Skupina",
                "verbose_name_plural": "Skupiny",
            },
        ),
    ]
