from email.mime import image

from django.db import models
from django.utils import timezone
from django.utils.datetime_safe import datetime
from enum import Enum


class ActionChoice(Enum):   # A subclass of Enum
    like: int = models.IntegerField()
    share: int = models.IntegerField()
    comment: str = models.CharField(max_length=255, blank=False, unique=True)


class User(models.Model):
    name: str = models.CharField(max_length=255, blank=False, unique=True)
    gender: str = models.CharField(max_length=20, blank=False, unique=True)
    address: str = ""
    status: str = ""
    mobile_number: int = models.IntegerField
    username: str = models.CharField(max_length=200)
    password: str = models.CharField(max_length=200)
    url: str = ""
    date_created: datetime = models.DateTimeField(auto_now=True, default=timezone.now)

    def __str__(self):
        return self.name


class Story(models.Model):
    title: str = models.CharField(max_length=255, blank= False, unique=True)
    description: str = models.CharField(max_length=255, blank=False, unique=True)
    language: str = models.CharField(max_length=255, blank=False, unique=True)
    status: str = models.CharField(max_length=255, blank=False, unique=True)
    moral: str = models.CharField()
    summary: str = models.CharField()
    categories: str = ""
    url: str = ""
    date_created = models.DateField("Date", default=datetime.date.today)
    thumbnail: image = models.ImageField()
    image: image = ""
    # a user can write multiple story
    user = models.ForeignKey(
        User,
        null=True,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.title


class Action(models.Model):
    action = [(tag, tag.value) for tag in ActionChoice]
    date_created = models.DateField("Date", default=datetime.date.today)
    # a story can have multiple action
    story = models.ForeignKey(
        Story,
        null=True,
        on_delete=models.CASCADE
    )
    user = models.ForeignKey(
        User,
        null=True,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.comment






