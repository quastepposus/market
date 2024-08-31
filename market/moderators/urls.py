from django.urls import path

from moderators import views

app_name = 'moderators'

urlpatterns = [
    path('advertisements/', views.AdvertisementListModeratorView.as_view(), name='advertisement_list'),
    path('advertisements/<int:pk>', views.AdvertisementDetailModeratorView.as_view(), name='advertisement_detail'),
]