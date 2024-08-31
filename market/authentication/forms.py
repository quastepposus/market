from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

User = get_user_model()


class UserSignupForm(UserCreationForm):
    usable_password = None

    class Meta:
        model = User
        fields = ('username', 'phone')
