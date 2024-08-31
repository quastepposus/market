from django.contrib.auth import get_user_model
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views import generic

from advertisements.models import Advertisement
from users.forms import UserInfoEditForm
from django.db.models import Q


class UserDetailView(generic.UpdateView):
    model = get_user_model()
    form_class = UserInfoEditForm

    def get_success_url(self):
        return reverse('users:profile', kwargs={'username': self.request.user.username})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['profile'] = get_object_or_404(get_user_model(), username=self.request.user.username)
        if self.request.user == context['profile']:
            context['advertisements'] = Advertisement.objects.filter(~Q(status='deleted'))
        else:
            context['advertisements'] = Advertisement.objects.filter(status='accepted')
        return context
