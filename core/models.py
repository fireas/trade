from django.contrib.auth import get_user_model
from django.conf import settings
from django.db import models
from django.shortcuts import reverse

# Create your models here.

GENRE_CHOICES = (
    ("1", "Aventure & Action"),
    ("2", "Classiques"),
    ("3", "Espionnage"),
    ("4", "Fantastique"),
    ("5", "Frisson & Terreur"),
    ("6", "Policier"),
    ("7", "Historique"),
    ("8", "Roman"),
    ("9", "Science-Fiction"),
    ("10", "Thriller"),
    ("11", "Mangas"),
    ("12", "Humour"),
    ("13", "Politique")
)


TRADETYPE_CHOICES = (
    ("S", "Sale"),
    ("T", "Trade"),
    ("G", "Giveaway")
)


class Book(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=50, null=False, blank=False)
    author = models.CharField(max_length=50)
    image = models.ImageField()
    genre = models.CharField(max_length=2, choices=GENRE_CHOICES)
    tradeType = models.CharField(max_length=1, choices=TRADETYPE_CHOICES)
    price = models.FloatField(null=True, blank=True)
    description = models.TextField(max_length=1000)
     
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("core:book", kwargs={"pk": self.pk})

