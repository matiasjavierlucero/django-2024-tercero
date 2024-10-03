from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    language = models.CharField(
        max_length=30,
        choices=[
            ('en', 'English'),
            ('es', 'Español'),
        ],
        default='es',
    )
