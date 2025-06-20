from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Reservation

def home(request):
    return render(request, 'index.html')

def reservation(request):
    if request.method == 'POST':
        name = request.POST.get('booking-form-name')
        phone = request.POST.get('booking-form-phone')
        date = request.POST.get('booking-form-date')
        time = request.POST.get('booking-form-time')
        number_of_people = request.POST.get('booking-form-number')
        message = request.POST.get('booking-form-message')

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

    return render(request, 'reservation.html')

def success(request):
    return render(request, 'success.html')
