from django.db import models
# Create your models here.


class User(models.Model):
    first_name = models.CharField(max_length=255, blank=False, unique=True)
    last_name = models.CharField(max_length=255, blank=False, unique=True)

class Story(models.Model):
    title = models.CharField(max_length=255, blank= False, unique=True)
    description = models.CharField(max_length=255, blank=False, unique=True)






