from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    # User fields

    first_name = models.CharField(max_length=150, editable=False)
    last_name = models.CharField(max_length=150, editable=False)

    name = models.CharField(max_length=150, default="")
    profile_img = models.URLField(max_length=200)
    profile_introduce = models.CharField(max_length=100)
    follower_num = models.PositiveIntegerField(default=0)
    following_num = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name  # or any other field you'd like to represent this user
