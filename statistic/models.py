from django.db import models

# Create your models here.

class CountryData(models.Model):
    contry = models.CharField(max_length=100)
    population = models.IntegerField()

    class Meta:
        verbose_name_plural = 'Country Population Data'

    def __str__(self) -> str:
        return f"{self.contry} ({self.population})"