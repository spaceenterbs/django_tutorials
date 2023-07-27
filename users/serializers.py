from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"
        # fields = (
        #     "id",
        #     "caption",
        #     "contentImg",
        #     "likesNum",
        #     "feeds_category",
        # )
        # exclude = ("created_at", "updated_at")
