from django.contrib import admin

from .models import Orcamentos, OrcamentosItens


class OrcamentosItensInline(admin.TabularInline):
    model = OrcamentosItens
    extra = 0


@admin.register(Orcamentos)
class OrcamentosAdmin(admin.ModelAdmin):
    inlines = (OrcamentosItensInline,)
    list_display = ('__str__',)
    # readonly_fields = ('slug',)
    # list_display_links = ('name',)
    # search_fields = ('name',)
    # list_filter = ('type',)
    # date_hierarchy = 'created'
    # ordering = ('-created',)
    # actions = ('',)
