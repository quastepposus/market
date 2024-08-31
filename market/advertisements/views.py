from django.contrib.auth.mixins import UserPassesTestMixin
from django.urls import reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from advertisements.forms import AdvertisementForm
from advertisements.models import Advertisement


class AdvertisementListView(ListView):
    model = Advertisement
    context_object_name = 'advertisements'
    template_name = 'advertisements/advertisement_list.html'

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(is_active=True, status='accepted').order_by('-publicate_time')

class AdvertisementCreateView(UserPassesTestMixin, CreateView):
    model = Advertisement
    form_class = AdvertisementForm
    template_name = 'advertisements/advertisement_create.html'

    def test_func(self):
        return self.request.user.is_authenticated

    def form_valid(self, form):
        form.instance.status = 'moderation'
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('advertisements:detail', kwargs={'pk': self.object.pk})

class AdvertisementDetailView(DetailView):
    model = Advertisement
    template_name = 'advertisements/advertisement_detail.html'

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(is_active=True)

    def get_success_url(self):
        return reverse('advertisements:detail', kwargs={'pk': self.object.pk})

class AdvertisementUpdateView(UserPassesTestMixin, UpdateView):
    model = Advertisement
    form_class = AdvertisementForm
    template_name = 'advertisements/advertisement_update.html'

    def test_func(self):
        return self.request.user == self.get_object().author

    def get_success_url(self):
        return reverse('advertisements:detail', kwargs={'pk': self.object.pk})

class AdvertisementDeleteView(UserPassesTestMixin, DeleteView):
    model = Advertisement
    template_name = 'advertisements/advertisement_detail.html'

    def get_success_url(self):
        return reverse('advertisements:list')

    def test_func(self):
        return self.request.user == self.get_object().author
