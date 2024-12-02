# account/admin.py
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserCreationForm

from .models import User, Profile
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

# class CustomUserCreationForm(UserCreationForm):
#     pass
class CustomUserAdmin(UserAdmin):
    # add_form = CustomUserCreationForm
    model = User
    list_display = ('email', 'is_active', 'is_superuser', 'is_staff')
    list_filter = ('email', 'is_superuser', 'is_active')
    search_fields = ('email',)
    ordering = ('email',)
    fieldsets = (
        ("Authentication", {'fields': ('email', 'password')}), #نام گذاری دل به خواه است
        ("permissions", {'fields': ('is_active', 'is_superuser', 'is_staff')}),
        # ("group permissions", {'fields': ('group', 'user_permissions')}),
        ("important dates", {'fields': ('last_login',)}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'is_active', 'is_superuser', 'is_staff')
        }),
    )

admin.site.register(User, CustomUserAdmin)
admin.site.register(Profile)