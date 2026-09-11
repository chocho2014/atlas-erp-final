from django.contrib import admin
from .models import Marca


@admin.register(Marca)
class MarcaAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "nombre",
        "estado",
        "fecha_creacion",
    )

    search_fields = (
        "nombre",
    )

    list_filter = (
        "estado",
    )