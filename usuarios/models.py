from django.db import models

# Create your models here.
class Usuario(models.Model):
    nome = models.CharField(max_length=255, null=False)
    email = models.CharField(max_length=255, null=False)
    senha = models.CharField(max_length=20, null=False)
    nick = models.CharField(max_length=30, null=False)
