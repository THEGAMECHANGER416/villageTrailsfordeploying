from django.contrib import admin
from .models import Listing


# Register your models here.
@admin.register(Listing)
class ListingAdmin(admin.ModelAdmin):
    list_display = [
        'id', 'name', 'description', 'state', 'isActive', 'startDate', 'endDate', 'hostId',
        'guestId', 'cost', 'createdAt'
    ]
