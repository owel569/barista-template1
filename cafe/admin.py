from django.contrib import admin
<<<<<<< HEAD
from .models import Reservation

@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'date', 'time', 'number_of_people', 'status', 'created_at')
    list_filter = ('status', 'date')
    search_fields = ('name', 'phone', 'message')
    ordering = ('-created_at',)
    readonly_fields = ('created_at',)
    
    fieldsets = (
        (None, {
            'fields': ('name', 'phone', 'date', 'time', 'number_of_people', 'message', 'status')
        }),
        ('Informations additionnelles', {
            'fields': ('created_at',),
        }),
    )
=======
from .models import MenuItem, Reservation, Testimonial, Contact

@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'price', 'available', 'created_at']
    list_filter = ['category', 'available']
    search_fields = ['name', 'description']
    ordering = ['category', 'name']

@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'date', 'time', 'guests', 'status', 'created_at']
    list_filter = ['status', 'date', 'created_at']
    search_fields = ['name', 'email', 'phone']
    ordering = ['-created_at']
    readonly_fields = ['created_at']

@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ['name', 'rating', 'approved', 'created_at']
    list_filter = ['rating', 'approved']
    search_fields = ['name', 'content']
    ordering = ['-created_at']

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'subject', 'created_at']
    search_fields = ['name', 'email', 'subject']
    ordering = ['-created_at']
    readonly_fields = ['created_at']
>>>>>>> ffce6af89a3517af95eb5d7be291ed190449e930
