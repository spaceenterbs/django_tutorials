from django.db import models
from common.models import CommonModel


class Review(CommonModel):
    # review fields
    r_caption = models.CharField(max_length=60)

    feed = models.ForeignKey("feeds.Feed", on_delete=models.CASCADE)
    user = models.ForeignKey("users.User", on_delete=models.CASCADE)

    def __str__(self):
        return self.r_caption  # or any other field you'd like to represent this user
