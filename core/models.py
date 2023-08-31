from django.db import models

# Create your models here.

class Empresa(models.Model):
    cnpj = models.CharField(max_length=20)
    razao_social = models.CharField(max_length=100)
    fantasia = models.CharField(max_length=100)
