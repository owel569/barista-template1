from django.contrib import admin
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
