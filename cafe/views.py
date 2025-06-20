from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import JsonResponse
from django.core.mail import mail_admins
# from .models import MenuItem, Reservation, Testimonial, Contact
from django.utils import timezone
from datetime import datetime
import json

def home(request):
    """Vue pour la page d'accueil"""
    # Données de démonstration statiques pour le moment
    menu_items = {
        'Café': [
            {'name': 'Espresso', 'description': 'Café italien classique', 'price': '2.50'},
            {'name': 'Cappuccino', 'description': 'Espresso avec mousse de lait', 'price': '3.50'},
            {'name': 'Latte', 'description': 'Café au lait doux', 'price': '4.00'},
        ],
        'Nourriture': [
            {'name': 'Croissant', 'description': 'Viennoiserie française', 'price': '2.00'},
            {'name': 'Sandwich Club', 'description': 'Sandwich complet avec salade', 'price': '8.50'},
        ],
        'Dessert': [
            {'name': 'Tiramisu', 'description': 'Dessert italien au café', 'price': '5.50'},
        ],
        'Boissons': [
            {'name': 'Jus d\'orange', 'description': 'Jus de fruits frais', 'price': '3.00'},
        ]
    }
    
    testimonials = [
        {'name': 'Marie Dubois', 'content': 'Excellents cafés et ambiance chaleureuse ! Je recommande vivement ce lieu.', 'rating': 5, 'image': None},
        {'name': 'Pierre Martin', 'content': 'Le meilleur café de la ville, service impeccable et produits de qualité.', 'rating': 5, 'image': None},
        {'name': 'Sophie Laurent', 'content': 'Un endroit parfait pour travailler ou se détendre. J\'adore leur tiramisu !', 'rating': 4, 'image': None},
    ]
    
    # Traiter le formulaire de contact
    if request.method == 'POST':
        messages.success(request, 'Merci pour votre message ! Nous vous répondrons bientôt.')
        return redirect('home')
    
    context = {
        'menu_items': menu_items,
        'testimonials': testimonials,
    }
    return render(request, 'home.html', context)

def reservation(request):
    """Vue pour la page de réservation"""
    if request.method == 'POST':
        try:
            name = request.POST.get('name')
            date = request.POST.get('date')
            time = request.POST.get('time')
            
            messages.success(request, 
                f'Réservation créée avec succès pour {name} le {date} à {time}.')
            return redirect('reservation')
            
        except Exception as e:
            messages.error(request, 'Erreur lors de la création de la réservation. Veuillez réessayer.')
    
    # Données de démonstration pour les réservations récentes
    recent_reservations = [
        {'name': 'Jean Dupont', 'date': '2025-06-21', 'time': '19:00', 'guests': 2, 'status': 'confirmed', 'get_status_display': 'Confirmée'},
        {'name': 'Marie Claire', 'date': '2025-06-22', 'time': '20:00', 'guests': 4, 'status': 'pending', 'get_status_display': 'En attente'},
    ]
    
    context = {
        'recent_reservations': recent_reservations,
    }
    return render(request, 'reservation.html', context)

def contact(request):
    """Vue pour traiter le formulaire de contact"""
    if request.method == 'POST':
        messages.success(request, 'Merci pour votre message ! Nous vous répondrons bientôt.')
    
    return redirect('home')

def api_reservations(request):
    """API pour récupérer les réservations (pour usage futur)"""
    if request.method == 'GET':
        data = []
        return JsonResponse({'reservations': data})
    
    return JsonResponse({'error': 'Method not allowed'}, status=405)
