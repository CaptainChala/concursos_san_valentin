from django.contrib import admin
from .models import Participante, User


@admin.register(Participante)
class ParticipanteAdmin(admin.ModelAdmin):
    list_display = ("nombre_completo", "email", "telefono", "verificado", "creado_en")
    search_fields = ("nombre_completo", "email")
    list_filter = ("verificado",)


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ("username", "email", "is_admin", "is_active", "is_staff")
    search_fields = ("username", "email")
    list_filter = ("is_admin", "is_staff", "is_active")
