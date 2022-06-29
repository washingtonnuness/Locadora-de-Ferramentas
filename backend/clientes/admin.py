from django.contrib import admin

from .models import Clientes


class ClientesAdmin(admin.ModelAdmin):
    readonly_fields = ("created_at", "updated_at", "delete_at")
    list_display = [f.name for f in Clientes._meta.fields]


admin.site.register(Clientes, ClientesAdmin)
