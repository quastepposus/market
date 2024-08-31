from django.views.generic import ListView, DetailView

from advertisements.models import Advertisement


class AdvertisementListModeratorView(ListView):
    model = Advertisement
    template_name = 'advertisement_list_moderation.html'
    context_object_name = 'advertisements'

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(status='moderation', is_active=True).order_by('create_time')

class AdvertisementDetailModeratorView(DetailView):
    model = Advertisement
    template_name = 'advertisement_detail_moderation.html'
    context_object_name = 'advertisement'

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(status='moderation', is_active=True)

