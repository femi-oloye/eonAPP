from django.contrib import admin
# accounts/admin.py
from django.contrib import admin
from .models import TelemarketData

# Register TelemarketData model to the admin interface
@admin.register(TelemarketData)
class TelemarketDataAdmin(admin.ModelAdmin):
    list_display = ('user', 'date', 'dialed_contacts', 'connected_calls', 'credited_amount', 'referred_contacts', 'feedback')
    list_filter = ('date', 'user')  # Filters for the data
    search_fields = ('user__username', 'feedback')  # Allow search by user and feedback

# Register your models here.
