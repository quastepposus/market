from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.views import generic

from advertisements.models import Advertisement
from users.forms import UserInfoEditForm
from django.db.models import Q


class UserDetailView(generic.UpdateView):
    model = get_user_model()
    form_class = UserInfoEditForm
    template_name = 'user_detail.html'

    def get_success_url(self, **kwargs):
        return reverse('users:detail', kwargs={'pk': self.object.id})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = get_object_or_404(get_user_model(), pk=self.object.id)
        if self.request.user == context['user']:
            context['advertisements'] = Advertisement.objects.filter(~Q(status='deleted'))
        else:
            context['advertisements'] = Advertisement.objects.filter(status='accepted')
        return context
