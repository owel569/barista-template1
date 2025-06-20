from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import JsonResponse
from django.utils import timezone
from datetime import datetime

from .models import Reservation  # ajoute d'autres si besoin

def home(request):
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
    
    if request.method == 'POST':
        messages.success(request, 'Merci pour votre message ! Nous vous répondrons bientôt.')
        return redirect('home')
    
    context = {
        'menu_items': menu_items,
        'testimonials': testimonials,
    }
    return render(request, 'home.html', context)

def reservation(request):
    if request.method == 'POST':
        name = request.POST.get('booking-form-name') or request.POST.get('name')
        phone = request.POST.get('booking-form-phone')
        date = request.POST.get('booking-form-date') or request.POST.get('date')
        time = request.POST.get('booking-form-time') or request.POST.get('time')
        number_of_people = request.POST.get('booking-form-number') or request.POST.get('guests')
        message = request.POST.get('booking-form-message') or ''

        if not all([name, phone, date, time, number_of_people]):
            messages.error(request, 'Tous les champs obligatoires doivent être remplis.')
            return render(request, 'reservation.html')

        try:
            number_of_people = int(number_of_people)
        except ValueError:
            messages.error(request, 'Le nombre de personnes doit être un chiffre valide.')
            return render(request, 'reservation.html')

        try:
            Reservation.objects.create(
                name=name,
                phone=phone,
                date=date,
                time=time,
                number_of_people=number_of_people,
                message=message
            )
            messages.success(request, 'Votre réservation a été enregistrée avec succès !')
            return redirect('cafe:success')

        except Exception:
            messages.error(request, "Une erreur est survenue. Veuillez réessayer plus tard.")

    # Affiche les réservations récentes (exemple)
    recent_reservations = Reservation.objects.order_by('-created_at')[:5]
    
    context = {
        'recent_reservations': recent_reservations,
    }
    return render(request, 'reservation.html', context)

def success(request):
    return render(request, 'success.html')

def contact(request):
    if request.method == 'POST':
        messages.success(request, 'Merci pour votre message ! Nous vous répondrons bientôt.')
    return redirect('home')

def api_reservations(request):
    if request.method == 'GET':
        reservations = list(Reservation.objects.values())
        return JsonResponse({'reservations': reservations})
    return JsonResponse({'error': 'Method not allowed'}, status=405)
