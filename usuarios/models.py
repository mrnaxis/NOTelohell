from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Usuario(models.Model):
    nome = models.CharField(max_length=100, null=False)
    nick = models.CharField(max_length=30, null=False)
    usuario = models.OneToOneField(User, related_name="usuario")
