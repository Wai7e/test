from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone
from django.db.models import F, Sum

User = get_user_model()


class Book(models.Model):
    title = models.CharField(max_length=256)
    author = models.CharField(max_length=256)
    category = models.CharField(max_length=256)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name='Пользователь'
    )
