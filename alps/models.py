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

    title = models.CharField(max_length=150)
    category = models.CharField(max_length=150, null=False, choices=CHOICES)
    discription = models.CharField(max_length=350)
    text = models.TextField(blank=True)
    image = models.ImageField(upload_to='portfolio/images/')
    url = models.URLField(blank=True)

    def __str__(self):
        return self.title


class Contact(models.Model):
    name = models.CharField(max_length=150)
    street = models.CharField(max_length=150)
    phone = models.CharField(max_length=150)
    partitaiva = models.CharField(max_length=150)
    email = models.CharField(max_length=150)
    homepage = models.CharField(max_length=150, blank=True)


    emailbluchalet = models.CharField(max_length=150)
    phonebluchalet = models.CharField(max_length=150)

    def __str__(self):
        return self.name
