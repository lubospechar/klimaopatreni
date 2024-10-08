# Generated by Django 5.0.7 on 2024-08-02 14:46

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("dbklima", "0011_subgroup_env"),
    ]

    operations = [
        migrations.AddField(
            model_name="subgroup",
            name="env_secondary",
            field=models.ManyToManyField(
                limit_choices_to={"choice_name_id": 1},
                related_name="envs_sec",
                to="dbklima.choice",
                verbose_name="Složka ŽP (přesah)",
            ),
        ),
        migrations.AlterField(
            model_name="subgroup",
            name="env",
            field=models.ForeignKey(
                blank=True,
                limit_choices_to={"choice_name_id": 1},
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="envs",
                to="dbklima.choice",
                verbose_name="Složka ŽP",
            ),
        ),
    ]
