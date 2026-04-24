from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

class CustomUser(AbstractUser):
    email = models.EmailField(_("email address"), unique=True)
    password_hash = models.CharField(max_length=15, unique=True)

    def __str__(self):
        return f"{self.username.title()}"
