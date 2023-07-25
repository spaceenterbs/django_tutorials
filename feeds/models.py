from django.db import models
from common.models import CommonModel


class Feed(CommonModel):  # 하나의 모델 without -s
    # common fields
    caption = models.CharField(max_length=120)  # 게시글 내용
    contentImg = models.URLField(blank=True)  # 게시글 이미지
    likesNum = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.caption  # or any other field you'd like to represent this user
