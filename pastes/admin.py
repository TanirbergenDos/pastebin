from django.contrib import admin
from .models import Paste


@admin.register(Paste)
class PasteAdmin(admin.ModelAdmin):
    list_display = ["text", "url", "created_at", "expired_at"]
