from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser
from django.utils.html import format_html

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    fieldsets = UserAdmin.fieldsets + (
        ('Additional Info', {
            'fields': ('profile_image', 'phone_number', 'national_code'),
        }),
    )
    list_display = ['username', 'email', 'phone_number', 'national_code', 'image_preview']
    def image_preview(self, obj):
        if obj.profile_image:
            return format_html('<img src="{}" style="width: 50px; height: 50px;" />', obj.profile_image.url)
        return "No Image"

    image_preview.short_description = "Profile Image"
admin.site.register(CustomUser, CustomUserAdmin)