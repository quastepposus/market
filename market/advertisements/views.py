from django.urls import reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from advertisements.forms import AdvertisementForm
from advertisements.models import Advertisement


class AdvertisementListView(ListView):
    model = Advertisement
    context_object_name = 'advertisements'
    template_name = 'advertisement_list.html'

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(active=True, status='accepted').order_by('-publicate_time')

class AdvertisementDetailView(DetailView):
    model = Advertisement
    context_object_name = 'advertisement'
    template_name = 'advertisement_detail.html'

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(active=True, status='accepted')

class AdvertisementCreateView(CreateView):
    model = Advertisement
    form_model = AdvertisementForm
    template_name = 'advertisement_create.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('advertisement:detail', kwargs={'pk': self.object.pk})

class AdvertisementUpdateView(UpdateView):
    model = Advertisement
    form_model = AdvertisementForm
    template_name = 'advertisement_detail.html'

    def get_success_url(self):
        return reverse('advertisement:detail', kwargs={'pk': self.object.pk})

class AdvertisementDeleteView(DeleteView):
    model = Advertisement
    template_name = 'advertisement_detail.html'

    def get_success_url(self):
        return reverse('advertisement:list')

