from django.contrib import admin
from .models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "username",
        "name",
        "profile_img",
        "profile_introduce",
        "follower_num",
        "following_num",
        "is_business",
    )
