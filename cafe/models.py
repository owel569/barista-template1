from django.db import models
<<<<<<< HEAD
from django.core.exceptions import ValidationError
from django.utils import timezone
=======
from django.core.validators import RegexValidator
import uuid

class MenuItem(models.Model):
    CATEGORY_CHOICES = [
        ('coffee', 'Café'),
        ('food', 'Nourriture'),
        ('dessert', 'Dessert'),
        ('drink', 'Boissons'),
    ]
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    image = models.ImageField(upload_to='menu/', blank=True, null=True)
    available = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['category', 'name']
>>>>>>> ffce6af89a3517af95eb5d7be291ed190449e930

class Reservation(models.Model):
    STATUS_CHOICES = [
        ('pending', 'En attente'),
        ('confirmed', 'Confirmée'),
        ('cancelled', 'Annulée'),
    ]
<<<<<<< HEAD

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
=======
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_regex = RegexValidator(
        regex=r'^\+?[1-9]\d{1,14}$', 
        message="Le numéro de téléphone doit être au format: '+999999999'. Jusqu'à 15 chiffres autorisés."
    )
    phone = models.CharField(validators=[phone_regex], max_length=17)
    date = models.DateField()
    time = models.TimeField()
    guests = models.PositiveIntegerField()
    special_requests = models.TextField(blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.name} - {self.date} {self.time}"
    
    class Meta:
        ordering = ['-created_at']

class Testimonial(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    content = models.TextField()
    rating = models.PositiveIntegerField(choices=[(i, i) for i in range(1, 6)], default=5)
    image = models.ImageField(upload_to='testimonials/', blank=True, null=True)
    approved = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.name} - {self.rating} étoiles"
    
    class Meta:
        ordering = ['-created_at']

class Contact(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.name} - {self.subject}"
    
    class Meta:
        ordering = ['-created_at']
>>>>>>> ffce6af89a3517af95eb5d7be291ed190449e930
