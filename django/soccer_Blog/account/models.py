from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(AbstractUser) :
    favorite_club = models.CharField(max_length=100, blank=True)
    nationality = models.CharField(max_length=100, blank=True)
    age = models.IntegerField(blank=True, default=0)