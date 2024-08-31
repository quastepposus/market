from django.contrib.auth.models import AbstractUser
from django.db import models

from users.validators import phone_for_user


class CustomUser(AbstractUser):
    phone = models.CharField(max_length=20, unique=True, validators=[phone_for_user, ])