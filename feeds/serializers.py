from rest_framework import serializers
from .models import Feed

from users.serializers import UserSerializer


class FeedSerializer(serializers.ModelSerializer):
    # Feed는 User의 자녀니가 직접 접근이 가능. (FK, N)
    user = UserSerializer()

    class Meta:
        model = Feed
        fields = "__all__"
        # fields = (
        #     "id",
        #     "caption",
        #     "contentImg",
        #     "likesNum",
        #     "feeds_category",
        # )
        # exclude = ("created_at", "updated_at")
