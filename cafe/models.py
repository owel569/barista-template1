from django.db import models
from django.core.exceptions import ValidationError
from django.utils import timezone

class Reservation(models.Model):
    STATUS_CHOICES = [
        ('pending', 'En attente'),
        ('confirmed', 'Confirmée'),
        ('cancelled', 'Annulée'),
    ]

    name = models.CharField("Nom", max_length=100)
    phone = models.CharField("Téléphone", max_length=20)
    date = models.DateField("Date de réservation")
    time = models.TimeField("Heure de réservation")
    number_of_people = models.IntegerField("Nombre de personnes")
    message = models.TextField("Message", blank=True, null=True)
    status = models.CharField(
        "Statut", max_length=10, choices=STATUS_CHOICES, default='pending'
    )
    created_at = models.DateTimeField("Créé le", auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name = "Réservation"
        verbose_name_plural = "Réservations"

    def __str__(self):
        return f"{self.name} - {self.date} à {self.time} ({self.status})"

    def clean(self):
        if self.date < timezone.now().date():
            raise ValidationError("La date de réservation ne peut pas être dans le passé.")
