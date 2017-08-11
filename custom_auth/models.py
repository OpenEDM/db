from django.contrib.auth.models import AbstractUser
from django.db import models


class Company(models.Model):
    title = models.CharField(max_length=255)
    prefix = models.CharField(max_length=50, db_index=True, unique=True)

    def __str__(self):
        return self.title


class User(AbstractUser):
    company = models.ForeignKey(Company)

    class Meta(AbstractUser.Meta):
        swappable = 'AUTH_USER_MODEL'
