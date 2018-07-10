from email.mime import image

from django.db import models
from django.utils.datetime_safe import datetime


class User(models.Model):
    name: str = models.CharField(max_length=255, blank=False, unique=True)
    gender: str = models.CharField(max_length=20, blank=False, unique=True)
    address: str = ""
    status: str = ""
    mobile_number: int = models.IntegerField
    username: str = models.CharField(max_length=200)
    password: str = models.CharField(max_length=200)
    date_created: datetime = models.DateField("Date", default=datetime.date.today)

    def __str__(self):
        return self.name


class Story(models.Model):
    title: str = models.CharField(max_length=255, blank= False, unique=True)
    description: str = models.CharField(max_length=255, blank=False, unique=True)
    language: str = models.CharField(max_length=255, blank=False, unique=True)
    url: str = ""
    date_created = models.DateField("Date", default=datetime.date.today)
    thumbnail: image = models.ImageField()
    image: image = ""

    def __str__(self):
        return self.title


class Action(models.Model):
    like: int = models.IntegerField()
    share: int = models.IntegerField()
    comment: str = models.CharField(max_length=255, blank= False, unique=True)
    date_created= models.DateField("Date", default=datetime.date.today)

    def __str__(self):
        return self.comment






