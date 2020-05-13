from django.contrib.auth import get_user_model
from django.conf import settings
from django.db import models
from django.shortcuts import reverse

# Create your models here.

GENRE_CHOICES = (
    ("1", "Genre 1"),
    ("2", "Genre 2"),
    ("3", "Genre 3"),
    ("4", "Genre 4"),
    ("5", "Genre 5"),
    ("6", "Genre 6"),
    ("7", "Genre 7"),
    ("8", "Genre 8"),
    ("9", "Genre 9")
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

