from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser) :
    user_type = models.CharField(max_length=10, default='Admin')
    email = models.EmailField( max_length=254,unique=True)