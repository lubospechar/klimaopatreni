# Generated by Django 5.0.7 on 2024-09-27 10:49

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("dbklima", "0021_subgroup_price_subgroup_sdg_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="subgroup",
            name="unit",
            field=models.ForeignKey(
                limit_choices_to={"choice_name_id": 11},
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="units",
                to="dbklima.choice",
                verbose_name="Jednotka",
            ),
        ),
        migrations.AlterField(
            model_name="subgroup",
            name="quantification",
            field=models.ForeignKey(
                limit_choices_to={"choice_name_id": 5},
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="quantifications",
                to="dbklima.choice",
                verbose_name="Kvantifikace dopadu",
            ),
        ),
    ]
