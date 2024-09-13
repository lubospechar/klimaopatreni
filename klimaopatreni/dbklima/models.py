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


class ChoiceName(models.Model):
    choice_name = models.CharField(max_length=255, verbose_name="Název volby")

    class Meta:
        verbose_name = "Název volby"
        verbose_name_plural = "Názvy voleb"

    def __str__(self):
        return self.choice_name


class Choice(models.Model):
    choice_name = models.ForeignKey(
        ChoiceName, on_delete=models.CASCADE, verbose_name="Název volby"
    )
    choice = models.CharField(max_length=255, verbose_name="Volba")
    order = models.PositiveSmallIntegerField(verbose_name="Pořadí", default=0)
    description = models.TextField(verbose_name="Popis", null=True, blank=True)

    class Meta:
        verbose_name = "Volba"
        verbose_name_plural = "Volby"
        ordering = ["choice_name", "order"]

    def __str__(self):
        return f"{self.choice}"


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

    mix_localization = models.BooleanField(
        default=False, verbose_name="Přesah lokalizace extravilán - intravilán"
    )
    env = models.ForeignKey(
        Choice,
        on_delete=models.CASCADE,
        verbose_name="Složka ŽP",
        limit_choices_to={"choice_name_id": 1},
        related_name="envs",
    )
    env_secondary = models.ManyToManyField(
        Choice,
        verbose_name="Složka ŽP (přesah)",
        limit_choices_to={"choice_name_id": 1},
        related_name="envs_sec",
        blank=True,
    )

    potential = models.ForeignKey(
        Choice,
        verbose_name="Potenciál aplikace",
        limit_choices_to={"choice_name_id": 2},
        related_name="potentials",
        on_delete=models.CASCADE,
        null=True,
    )
    size = models.ForeignKey(
        Choice,
        verbose_name="Rozsah / velikost",
        limit_choices_to={"choice_name_id": 3},
        related_name="sizes",
        on_delete=models.CASCADE,
        null=True,
    )
    difficulty_of_implementation = models.ForeignKey(
        Choice,
        verbose_name="Náročnost realizace",
        limit_choices_to={"choice_name_id": 4},
        related_name="difficulty_of_implementations",
        on_delete=models.CASCADE,
        null=True,
    )
    conditions_for_implementation = models.TextField(
        verbose_name="Podmínky implementace", null=True, blank=False
    )

    def __str__(self):
        return f"{self.group}: {self.subgroup_name, self.code}"

    class Meta:
        unique_together = ("group", "subgroup_name")
        verbose_name = "Podskupina"
        verbose_name_plural = "Podskupiny"
