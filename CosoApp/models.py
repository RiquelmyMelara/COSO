# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

# Create your models here.
@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)

class COSO(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Componente(models.Model):
    nombre = models.CharField(max_length=100)
    peso = models.IntegerField(null=False)
    coso = models.ForeignKey(COSO)

    def __str__(self):
        return self.nombre

class Principio(models.Model):
    nombre = models.CharField(max_length=100)
    peso = models.IntegerField(null=False)
    componente = models.ForeignKey(Componente)

    def __str__(self):
        return self.nombre

class Enfoque(models.Model):
    nombre = models.CharField(max_length=100)
    peso = models.IntegerField(null=False)
    principio = models.ForeignKey(Principio)

    def __str__(self):
        return self.nombre

class Enunciados(models.Model):
    nombre = models.CharField(max_length=100)
    peso = models.IntegerField(null=False)
    principio = models.ForeignKey(Principio)

    def __str__(self):
        return self.nombre