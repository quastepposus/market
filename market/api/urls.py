from django.urls import path

from api import views

app_name = 'api'

urlpatterns = [
    path('advertiesments/<int:pk>/status/', views.AdvertisementStatusView.as_view(), name='advertisement_status'),
]