from django.db import models


class Activity(models.Model):
    name = models.CharField(max_length=250)


class InterestGroup(models.Model):
    name = models.CharField(max_length=250)
    is_active = models.BooleanField(default=True)


class Interest(models.Model):
    name = models.CharField(max_length=250)
    is_active = models.BooleanField(default=True)
    group = models.ForeignKey(InterestGroup, null=True, on_delete=models.SET_NULL)
    picture = models.ImageField()
