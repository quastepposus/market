from django.urls import path

from advertisements import views

app_name = 'advertisements'

urlpatterns = [
    path('', views.AdvertisementListView.as_view(), name='list'),
    path('<int:pk>/', views.AdvertisementDetailView.as_view(), name='detail'),
    path('<int:pk>/update', views.AdvertisementUpdateView.as_view(), name='update'),
    path('create/', views.AdvertisementCreateView.as_view(), name='create'),
    path('<int:pk>/delete/', views.AdvertisementDeleteView.as_view(), name='delete'),
]