from django.db import models

class Localization(models.Model):
    localization_name = models.CharField(max_length=30, verbose_name="Pojmenování lokalizace")

    def __str__(self):
        return self.localization_name

    class Meta:
        verbose_name = "Lokalizace"
        verbose_name_plural = "Lokalizace"

class Group(models.Model):
    localization = models.ForeignKey(Localization, on_delete=models.CASCADE, verbose_name="Lokalizace")
    group_name = models.CharField(max_length=30, verbose_name="Pojmenování skupiny")


    def __str__(self):
        return f'{self.localization}: {self.group_name}'

    class Meta:
        verbose_name = "Skupina"
        verbose_name_plural = "Skupiny"



