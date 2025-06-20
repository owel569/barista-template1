from django.urls import path
from . import views

<<<<<<< HEAD
app_name = 'cafe'

urlpatterns = [
    path('', views.home, name='home'),                 # Accueil, URL: /
    path('reservation/', views.reservation, name='reservation'),  # Formulaire réservation
    path('success/', views.success, name='success'),   # Page succès après réservation
]
=======
urlpatterns = [
    path('', views.home, name='home'),
    path('reservation/', views.reservation, name='reservation'),
    path('contact/', views.contact, name='contact'),
    path('api/reservations/', views.api_reservations, name='api_reservations'),
]
>>>>>>> ffce6af89a3517af95eb5d7be291ed190449e930
