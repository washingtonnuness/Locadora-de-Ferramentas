from django.contrib import admin

from .models import Cliente


class ClienteAdmin(admin.ModelAdmin):
    readonly_fields = ("created_at", "updated_at", "delete_at")
    list_display = [f.name for f in Cliente._meta.fields]


admin.site.register(Cliente, ClienteAdmin)
