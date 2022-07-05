from django.contrib import admin

from .models import Cliente

ADDRESS_FIELDS = (
    'address',
    'address_number',
    'complement',
    'district',
    'city',
    'uf',
    'cep',
)


class ClienteAdmin(admin.ModelAdmin):
    list_display = (
        'nome',
        'razao_social',
        'nome_fantasia',
        'tipo',
        'rg',
        'cpf',
        'cnpj',
        'endereco2',
        'delete_user',
    ) + ADDRESS_FIELDS
    readonly_fields = ('deleted',)
    list_display_links = ('nome',)
    search_fields = ('nome', 'razao_social', 'nome_fantasia')
    list_filter = ('tipo', 'uf', 'active')


admin.site.register(Cliente, ClienteAdmin)
