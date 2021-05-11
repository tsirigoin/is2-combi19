from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import Chofer, CustomUser

class CustomUserAdmin(UserAdmin):
	add_form = CustomUserCreationForm
	form = CustomUserChangeForm
	model = CustomUser
	list_display = (
		'email',
		'is_staff',
		'is_active',
	)
	list_filter = (
		'email',
		'is_staff',
		'is_active',
	)
	fieldsets = (
		(None,
			{
				'fields': (
					'email',
					'password',
				),
			}
		),
		('Información personal',
			{
				'fields': (
					'fecha_nacimiento',
				),
			}
		),
		('Permisos',
			{
				'fields': (
					'is_superuser',
					'is_active',
				),
			}
		),
	)
	add_fieldsets = (
		(None, {
			'classes': ('wide',),
			'fields': ('email','password1','password2','is_staff','is_active')},
		),
	)
	search_fields = (
		'email',
	)
	ordering = (
		'email',
	)
	filter_horizontal = ()

admin.site.register(CustomUser,CustomUserAdmin)
admin.site.register(Chofer)
admin.site.unregister(Group)