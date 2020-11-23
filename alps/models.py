from __future__ import unicode_literals
from django.db import models


# Create your models here.
class Activity(models.Model):
    CHOICES = (
        ('sport', 'Sport'),
        ('luoghi', "Luoghi d'interesse"),
        ('piatti', 'Piatti tipici'),
        ('after ski', 'After Ski'),
        ('cena', 'Cena in quota'),
    )

    category = models.CharField(max_length=150, null=False, choices=CHOICES)
    title = models.CharField(max_length=150)
    description = models.CharField(max_length=350)
    text = models.TextField(blank=True)
    image = models.ImageField(upload_to='portfolio/images/')
    url = models.URLField(blank=True)

    def __str__(self):
        return self.title


class Contact(models.Model):
    nameAdministrator = models.CharField(max_length=150)
    streetNumber = models.CharField(max_length=150)
    city = models.CharField(max_length=150)
    phone = models.CharField(max_length=150)
    partitaIva = models.CharField(max_length=150)
    email = models.CharField(max_length=150)

    emailBluchalet = models.CharField(max_length=150)
    phoneBluchalet = models.CharField(max_length=150)
    homepageBluchalet = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.nameAdministrator
