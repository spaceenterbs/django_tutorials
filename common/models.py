from django.db import models


class CommonModel(models.Model):
    # common fields
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)  # 수정되면 값이 병경됨

    class Meta:
        abstract = True
