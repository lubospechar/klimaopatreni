# Generated by Django 5.0.7 on 2024-08-02 14:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("dbklima", "0008_alter_choice_options_alter_choice_order"),
    ]

    operations = [
        migrations.AddField(
            model_name="subgroup",
            name="mix_localization",
            field=models.BooleanField(
                default=False, verbose_name="Přesah lokalizace extravilán - intravilán"
            ),
        ),
    ]
