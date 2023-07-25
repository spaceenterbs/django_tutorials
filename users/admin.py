from django.contrib import admin
from .models import User
from django.contrib.auth.admin import UserAdmin


# Register your models here.
@admin.register(User)
class UserAdmin(UserAdmin):
    fieldsets = (
        (
            "Profile Info",
            {
                "fields": (
                    "username",
                    "email",
                    "name",
                    "profile_img",
                    "profile_introduce",
                    "follower_num",
                    "following_num",
                ),
                "classes": ("wide",),
            },
        ),
        ("Permissions", {"fields": ("is_staff", "is_active", "is_superuser")}),
        ("Important dates", {"fields": ("last_login", "date_joined")}),
    )
    list_display = (
        "id",
        "username",
        "name",
        "profile_img",
        "profile_introduce",
        "follower_num",
        "following_num",
    )
    list_filter = ("username", "name")
    search_fields = ("username", "name")

    def get_readonly_fields(self, request, obj=None):
        if obj:  # editing an existing object
            return self.readonly_fields + ("first_name", "last_name")
        return self.readonly_fields
