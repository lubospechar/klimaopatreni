# Generated by Django 5.0.7 on 2024-10-02 07:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("dbklima", "0025_alter_example_location"),
    ]

    operations = [
        migrations.AddField(
            model_name="subgroup",
            name="env_desc",
            field=models.TextField(
                blank=True, null=True, verbose_name="Složka ŽP (přesah) - poznánka"
            ),
        ),
        migrations.AddField(
            model_name="subgroup",
            name="tag_desc",
            field=models.TextField(
                blank=True,
                null=True,
                verbose_name="Kategorie dopadu změny klimatu - poznánka",
            ),
        ),
    ]
