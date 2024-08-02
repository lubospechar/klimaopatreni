# Generated by Django 5.0.7 on 2024-08-02 14:17

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("dbklima", "0006_subgroup_advantages_subgroup_disadvantages"),
    ]

    operations = [
        migrations.CreateModel(
            name="ChoiceName",
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
                    "choice_name",
                    models.CharField(max_length=255, verbose_name="Název volby"),
                ),
            ],
            options={
                "verbose_name": "Název volby",
                "verbose_name_plural": "Názvy voleb",
            },
        ),
        migrations.CreateModel(
            name="Choice",
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
                ("choice", models.CharField(max_length=255, verbose_name="Volba")),
                ("order", models.PositiveSmallIntegerField(verbose_name="Pořadí")),
                ("description", models.TextField(verbose_name="Popis")),
                (
                    "choice_name",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="dbklima.choicename",
                        verbose_name="Název volby",
                    ),
                ),
            ],
            options={
                "verbose_name": "Volba",
                "verbose_name_plural": "Volby",
            },
        ),
    ]
