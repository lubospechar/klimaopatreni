from django.db import models


class Localization(models.Model):
    localization_name = models.CharField(
        max_length=30, verbose_name="Pojmenování lokalizace"
    )

    def __str__(self):
        return self.localization_name

    class Meta:
        verbose_name = "Lokalizace"
        verbose_name_plural = "Lokalizace"


class Group(models.Model):
    localization = models.ForeignKey(
        Localization, on_delete=models.CASCADE, verbose_name="Lokalizace"
    )
    group_name = models.CharField(max_length=30, verbose_name="Pojmenování skupiny")

    def __str__(self):
        return f"{self.localization}: {self.group_name}"

    class Meta:
        unique_together = ("localization", "group_name")
        verbose_name = "Skupina"
        verbose_name_plural = "Skupiny"


class Advantage(models.Model):
    description = models.CharField(
        max_length=255,
        verbose_name="Výhoda",
    )

    def __str__(self):
        return self.description

    class Meta:
        verbose_name = "Výhoda"
        verbose_name_plural = "Výhody"


class Disadvantage(models.Model):
    description = models.CharField(
        max_length=255,
        verbose_name="Nevýhoda",
    )

    def __str__(self):
        return self.description

    class Meta:
        verbose_name = "Nevýhoda"
        verbose_name_plural = "Nevýhody"

from django.db import models

class ChoiceName(models.Model):
    choice_name = models.CharField(max_length=255, verbose_name="Název volby")

    class Meta:
        verbose_name = "Název volby"
        verbose_name_plural = "Názvy voleb"

    def __str__(self):
        return self.choice_name


class Choice(models.Model):
    choice_name = models.ForeignKey(ChoiceName, on_delete=models.CASCADE, verbose_name="Název volby")
    choice = models.CharField(max_length=255, verbose_name="Volba")
    order = models.PositiveSmallIntegerField(verbose_name="Pořadí", default=0)
    description = models.TextField(verbose_name="Popis")

    class Meta:
        verbose_name = "Volba"
        verbose_name_plural = "Volby"
        ordering = ['choice_name', 'order']

    def __str__(self):
        return f"{self.choice_name} - {self.choice}"



class SubGroup(models.Model):
    group = models.ForeignKey(Group, on_delete=models.CASCADE, verbose_name="Skupina")
    subgroup_name = models.CharField(
        max_length=100, verbose_name="Pojmenování podskupiny"
    )
    code = models.CharField(max_length=10, verbose_name="Kód opatření", unique=True)
    abstract = models.CharField(max_length=255, verbose_name="Shrnutí opatření")
    description = models.TextField(
        verbose_name="Podrobný popis opatření",
        blank=False,
        null=False,
    )
    advantages = models.ManyToManyField(Advantage, verbose_name="Výhody")
    disadvantages = models.ManyToManyField(Disadvantage, verbose_name="Nevýhody")

    mix_localization = models.BooleanField(default=False, verbose_name="Přesah lokalizace extravilán - intravilán")

    def __str__(self):
        return f"{self.group}: {self.subgroup_name, self.code}"

    class Meta:
        unique_together = ("group", "subgroup_name")
        verbose_name = "Podskupina"
        verbose_name_plural = "Podskupiny"


