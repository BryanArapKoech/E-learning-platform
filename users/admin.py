from django.contrib import admin

# users/admin.py
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    # Add any custom fields to the admin display if you added them to the model
    # fieldsets = UserAdmin.fieldsets + (
    #     (None, {'fields': ('bio', 'profile_picture')}),
    # )
    # add_fieldsets = UserAdmin.add_fieldsets + (
    #     (None, {'fields': ('email',)}), # Ensure email is in add form if overridden
    # )
    pass # Keep it simple for now

admin.site.register(CustomUser, CustomUserAdmin)