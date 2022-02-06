from uuid import uuid4

from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    class Meta:
        ordering = ["uuid"]

    uuid = models.UUIDField(primary_key=True, default=uuid4)
    email = models.EmailField(unique=True, blank=False)
    birthday = models.DateField(null=True, blank=True)
