from django.contrib.auth import get_user_model
from django.contrib.auth.views import LoginView
from django.urls import reverse
from django.views.generic import CreateView

from authentication.forms import UserSignupForm


class SignupView(CreateView):
    model = get_user_model()
    form_class = UserSignupForm
    template_name = 'signup.html'

    def get_success_url(self):
        return reverse('auth:login')


class MyLoginView(LoginView):
    template_name = 'login.html'

    def get_success_url(self):
        return reverse('users:detail', kwargs={'pk': self.request.user.pk})

# class MyLogoutView(LogoutView):
#     success_url = reverse('index')

