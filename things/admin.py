"""Configuration of the admin interface for things."""
from django.contrib import admin
from .models import Thing

@admin.register(Thing)
class ThingsAdmin(admin.ModelAdmin):
    """Configuration of the admin interface for things"""

    list_display = [
        'name', 'description', 'quantity', 'created_at'
    ]
