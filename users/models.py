""" Django."""
from django.contrib.auth.models import User
from django.db import models


class Profile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    phone = models.CharField(max_length=20, blank=True, null=True)
    biography = models.TextField(blank=True)
    birthdate = models.DateField(null=True, blank=True)
    nationality = models.CharField(max_length=20, blank=True)

    picture = models.ImageField(
        upload_to='users',
        blank=True,
        null=True
    )

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username