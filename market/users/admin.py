from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from authentication.forms import UserSignupForm
from .forms import UserInfoEditForm
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    add_form = UserSignupForm
    form = UserInfoEditForm
    model = UserInfoEditForm
    list_display = ['email', 'username',]

admin.site.register(CustomUser, CustomUserAdmin)