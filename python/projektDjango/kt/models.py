from django.db import models

# Create your models here.


class Contact(models.Model):
    imie = models.CharField(max_length=50)
    nazwisko = models.CharField(max_length=100)
    email = models.EmailField()
    telefon = models.IntegerField()
