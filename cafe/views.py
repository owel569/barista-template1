from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import JsonResponse
from django.core.mail import mail_admins
from .models import MenuItem, Reservation, Testimonial, Contact
from django.utils import timezone
from datetime import datetime
import json

def home(request):
    """Vue pour la page d'accueil"""
    # Récupérer les éléments du menu par catégorie
    menu_items = {}
    for category_code, category_name in MenuItem.CATEGORY_CHOICES:
        items = MenuItem.objects.filter(category=category_code, available=True)[:4]
        if items:
            menu_items[category_name] = items
    
    # Récupérer les témoignages approuvés
    testimonials = Testimonial.objects.filter(approved=True)[:6]
    
    # Traiter le formulaire de contact
    if request.method == 'POST':
        contact = Contact(
            name=request.POST.get('name'),
            email=request.POST.get('email'),
            subject=request.POST.get('subject'),
            message=request.POST.get('message')
        )
        contact.save()
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
            # Créer une nouvelle réservation
            reservation = Reservation(
                name=request.POST.get('name'),
                email=request.POST.get('email'),
                phone=request.POST.get('phone'),
                date=request.POST.get('date'),
                time=request.POST.get('time'),
                guests=int(request.POST.get('guests')),
                special_requests=request.POST.get('special_requests', '')
            )
            reservation.save()
            
            messages.success(request, 
                f'Réservation créée avec succès pour {reservation.name} le {reservation.date} à {reservation.time}.')
            
            # Envoyer un email de notification (optionnel)
            try:
                mail_admins(
                    f'Nouvelle réservation - {reservation.name}',
                    f'Nouvelle réservation:\n\n'
                    f'Nom: {reservation.name}\n'
                    f'Email: {reservation.email}\n'
                    f'Téléphone: {reservation.phone}\n'
                    f'Date: {reservation.date}\n'
                    f'Heure: {reservation.time}\n'
                    f'Nombre de personnes: {reservation.guests}\n'
                    f'Demandes spéciales: {reservation.special_requests}\n'
                )
            except:
                pass  # Ignorer les erreurs d'email en développement
                
            return redirect('reservation')
            
        except Exception as e:
            messages.error(request, 'Erreur lors de la création de la réservation. Veuillez réessayer.')
    
    # Afficher les réservations récentes (pour démonstration)
    recent_reservations = Reservation.objects.all()[:6]
    
    context = {
        'recent_reservations': recent_reservations,
    }
    return render(request, 'reservation.html', context)

def contact(request):
    """Vue pour traiter le formulaire de contact"""
    if request.method == 'POST':
        contact = Contact(
            name=request.POST.get('name'),
            email=request.POST.get('email'),
            subject=request.POST.get('subject'),
            message=request.POST.get('message')
        )
        contact.save()
        messages.success(request, 'Merci pour votre message ! Nous vous répondrons bientôt.')
    
    return redirect('home')

def api_reservations(request):
    """API pour récupérer les réservations (pour usage futur)"""
    if request.method == 'GET':
        reservations = Reservation.objects.all()
        data = []
        for reservation in reservations:
            data.append({
                'id': str(reservation.id),
                'name': reservation.name,
                'email': reservation.email,
                'phone': reservation.phone,
                'date': reservation.date.isoformat(),
                'time': reservation.time.strftime('%H:%M'),
                'guests': reservation.guests,
                'status': reservation.status,
                'created_at': reservation.created_at.isoformat()
            })
        return JsonResponse({'reservations': data})
    
    return JsonResponse({'error': 'Method not allowed'}, status=405)
