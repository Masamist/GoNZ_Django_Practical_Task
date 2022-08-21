from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import CustomUser
from .forms import CustomUserCreationForm, CostomUserChangeForm

# Register your models here.


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CostomUserChangeForm

    model = CustomUser

    list_display = [
        "username",
        "roles",
        "email",
    ]

    fieldsets = UserAdmin.fieldsets + ((None, {"fields": ("roles", )}), )

    add_fieldsets = UserAdmin.add_fieldsets + \
        ((None, {"fields": ("roles", )}),)


admin.site.register(CustomUser, CustomUserAdmin)
