from django.db import models


class Comprador(models.Model):
    nome = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    compra = models.IntegerField()
