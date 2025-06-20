from django.urls import path
from . import views

app_name = 'cafe'

urlpatterns = [
    path('', views.home, name='home'),                 # Accueil, URL: /
    path('reservation/', views.reservation, name='reservation'),  # Formulaire réservation
    path('success/', views.success, name='success'),   # Page succès après réservation
]
