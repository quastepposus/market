from django.contrib.auth.views import LogoutView
from django.urls import path

from authentication import views

app_name = 'auth'

urlpatterns = [
    path('login/', views.MyLoginView.as_view(), name='login'),
    path('signup/', views.SignupView.as_view(), name='signup'),
    path('logout/', LogoutView.as_view(), name='logout'),
]