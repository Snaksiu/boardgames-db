from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="Nazwa kategorii")
    description = models.TextField(blank=True, verbose_name="Opis")

    class Meta:
        verbose_name = "Kategoria"
        verbose_name_plural = "Kategorie"
        ordering = ['name']

    def __str__(self):
        return self.name


class Game(models.Model):
    title = models.CharField(max_length=200, verbose_name="Tytuł gry")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='games', verbose_name="Kategoria")
    price = models.DecimalField(max_digits=6, decimal_places=2, verbose_name="Cena (PLN)")  # pole liczbowe
    release_date = models.DateField(verbose_name="Data premiery")  # pole datowe
    players_count = models.IntegerField(verbose_name="Maksymalna liczba graczy")
    description = models.TextField(verbose_name="Opis gry")

    class Meta:
        verbose_name = "Gra"
        verbose_name_plural = "Gry"
        ordering = ['title']

    def __str__(self):
        return self.title