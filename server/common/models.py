from django.db import models


class User(models.Model):
    name = models.CharField(max_length=15, default='')
    email = models.TextField(default='')
    password = models.CharField(max_length=20, default='')

    class Meta:
        ordering = ['id']


class Message(models.Model):
    message = models.TextField(default="")


class SignLogin(models.Model):
    name = models.CharField(max_length=15, default='')
    email = models.TextField(default='')
    password = models.CharField(max_length=20, default='')
