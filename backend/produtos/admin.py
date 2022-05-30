from django.contrib import admin

from .models import *

# Register your models here.


class ProdutosAdmin(admin.ModelAdmin):
    readonly_fields = ("created_at", "updated_at", "delete_at")
    list_display = [f.name for f in Produtos._meta.fields]
    search_fields = ('nome',)


class MarcaAdmin(admin.ModelAdmin):
    readonly_fields = ("created_at", "updated_at", "delete_at")
    list_display = [f.name for f in Marca._meta.fields]


class CategoriaAdmin(admin.ModelAdmin):
    readonly_fields = ("created_at", "updated_at", "delete_at")
    list_display = [f.name for f in Categoria._meta.fields]


class PatrimonioAdmin(admin.ModelAdmin):
    readonly_fields = ("created_at", "updated_at", "delete_at")
    list_display = [f.name for f in Patrimonio._meta.fields]


admin.site.register(Produtos, ProdutosAdmin)
admin.site.register(Marca, MarcaAdmin)
admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Patrimonio, PatrimonioAdmin)
