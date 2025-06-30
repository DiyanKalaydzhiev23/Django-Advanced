from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from accounts.forms import CustomUserCreationForm
from accounts.models import Profile

UserModel = get_user_model()


@admin.register(UserModel)
class UserModelAdmin(UserAdmin):
    list_display = ['username', 'email']
    add_form = CustomUserCreationForm

    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("username", "email", "password1", "password2"),
            },
        ),
    )

    fieldsets = (
        (None, {"fields": ("username", "password")}),
        ("Personal info", {"fields": ("email",)}),
        (
            "Permissions",
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        ("Important dates", {"fields": ("last_login",)}),
    )


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    ...
