from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import Chofer, CustomUser

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ('username', 'is_staff', 'is_active',)
    list_filter = ('username    ', 'is_staff', 'is_active',)
    fieldsets = (
        (None, {'fields': ('username','first_name', 'last_name','email','password1','password2','fecha_nacimiento')}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username','first_name', 'last_name','email','password1','password2','fecha_nacimiento','is_staff','is_active')}
        ),
    )
    search_fields = ('username',)
    ordering = ('username',)

admin.site.register(CustomUser)
admin.site.register(Chofer)
admin.site.unregister(Group)