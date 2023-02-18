from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField(upload_to='media')
    description = models.TextField(null=False, blank=False, max_length=250)

    def __str__(self):
        return self.user.username
