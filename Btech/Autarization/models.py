from django.db import models

class Registration(models.Model):
    email = models.CharField(max_length=100)
    number = models.IntegerField(blank=True, null=True)


class Autorization(models.Model):
    email = models.CharField(max_length=100)
    number = models.IntegerField(blank=True, null=True)