from django.contrib import admin
from django.contrib.auth import get_user_model

UserModel = get_user_model()

@admin.register(UserModel)
class UserModelAdmin(admin.ModelAdmin):
    pass
