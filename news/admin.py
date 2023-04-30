from django.contrib import admin
from .models import New

@admin.register(New)
class LigaAdmin(admin.ModelAdmin):
    list_display = ["name"]
