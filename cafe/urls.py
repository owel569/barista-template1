from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('reservation/', views.reservation, name='reservation'),
    path('contact/', views.contact, name='contact'),
    path('api/reservations/', views.api_reservations, name='api_reservations'),
]