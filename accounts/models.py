from django.db import models
from django.contrib.auth.models import AbstractUser           #abstract class vs interface

# Create your models here.
class Role(models.Model):
    name = models.CharField(max_length=128)
    description = models.CharField(max_length=256)

    def __str__(self):
        return self.name

class Team(models.Model):
    name = models.CharField(max_length=128)
    description = models.CharField(max_length=256)

    def __str__(self):
        return self.name

class CustomUser(AbstractUser):
    role = models.ForeignKey(
        Role,
        on_delete=models.SET_NULL,
        blank=True, null=True
    )
    team = models.ForeignKey(
        Team,
        on_delete=models.SET_NULL,
        blank=True, null=True
    )