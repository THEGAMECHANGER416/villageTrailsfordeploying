from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import VTUser

# Register your models here.
@admin.register(VTUser)
class VTUserAdmin(UserAdmin):
    fieldsets = (
        (None, {'fields': ('phone',)}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('phone','is_staff', 'is_active')}
         ),
    )
    list_filter = ['phone']
    list_display = [
        'id',
        'name',
        'phone',
        'is_guest',
        'otp',
        'createdAt'
    ]
    ordering = ['phone']
    search_fields = ('phone','name',)
    filter_horizontal = ()
