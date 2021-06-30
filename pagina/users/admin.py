from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin

from django.utils.translation import ugettext_lazy as _

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import Chofer, CustomUser

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser

    fieldsets = (
        (None, {'fields': ('username','first_name', 'last_name','email','password1','password2','fecha_nacimiento')}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username','first_name', 'last_name','email','password1','password2','fecha_nacimiento',)}
        ),
    )
    list_display = ('username','first_name','last_name','email','fecha_nacimiento')
    search_fields = ('username','first_name','last_name','email')
    ordering = ('username',)

    def get_form(self, request, obj=None, **kwargs):
         form = super(CustomUserAdmin,self).get_form(request, obj, **kwargs)
         return form

admin.site.register(CustomUser,CustomUserAdmin)
@admin.register(Chofer)
class ChoferAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'dni',
        'contacto',
    )
admin.site.unregister(Group)

"""@admin.register(Tarjeta)
class TarjetaAdmin"""