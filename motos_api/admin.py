from django.contrib import admin
from .models import Moto

class MotoAdmin(admin.ModelAdmin):
    list_display = (
        "reference",
        "trademark",
        "model",
        "price",
        "image",
        "supplier",
    )

admin.site.register(Moto, MotoAdmin)