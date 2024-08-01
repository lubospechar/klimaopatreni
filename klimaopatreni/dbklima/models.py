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

    def __str__(self):
        return f"{self.group}: {self.subgroup_name, self.code}"

    class Meta:
        unique_together = ("group", "subgroup_name")
        verbose_name = "Podskupina"
        verbose_name_plural = "Podskupiny"
