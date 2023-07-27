from .models import Review
from rest_framework.serializers import ModelSerializer
from users.serializers import UserSerializer


class ReviewSerializer(ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Review
        fields = "__all__"
