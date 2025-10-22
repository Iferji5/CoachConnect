# accounts/admin.py
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin
from .models import User, TrainerProfile, AthleteProfile

class TrainerInline(admin.StackedInline):
    model = TrainerProfile
    can_delete = False
    extra = 0

class AthleteInline(admin.StackedInline):
    model = AthleteProfile
    can_delete = False
    extra = 0

@admin.register(User)
class UserAdmin(DjangoUserAdmin):
    # columnas de la tabla
    list_display = ("username", "email", "role", "is_active", "is_staff", "date_joined", "last_login")
    list_filter  = ("role", "is_active", "is_staff")
    search_fields = ("username", "email")
    readonly_fields = ("date_joined", "last_login")
    inlines = [TrainerInline, AthleteInline]

    # añade nuestros campos a los formularios de edición/alta
    fieldsets = DjangoUserAdmin.fieldsets + (
        ("Perfil", {"fields": ("role", "timezone", "language")}),
    )
    add_fieldsets = DjangoUserAdmin.add_fieldsets + (
        (None, {"fields": ("role", "timezone", "language", "email")}),
    )
