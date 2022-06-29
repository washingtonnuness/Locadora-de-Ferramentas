from django.db import models

from backend.clientes.models import Clientes
from backend.produtos.models import Patrimonio, Produtos


class Orcamentos(models.Model):

    cliente = models.ForeignKey(
        Clientes,
        on_delete=models.SET_NULL,
        related_name='cliente_orcamentos',
        null=True,
        blank=True
    )

    created_user = models.CharField(
        max_length=100,
        null=True,
        blank=True
    )

    delete_user = models.CharField(
        max_length=100,
        null=True,
        blank=True
    )

    checkbox = models.BooleanField(
        "Excluir",
        max_length=10
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    delete_at = models.DateTimeField(
        null=True,
        blank=True
    )

    class Meta:
        ordering = ('created_at',)
        verbose_name = "Orçamento"
        verbose_name_plural = "Orçamentos"

    def __str__(self):
        return f'{self.pk}'


class OrcamentosItens(models.Model):
    orcamento = models.ForeignKey(
        Orcamentos,
        on_delete=models.CASCADE,
        related_name='orcamentos',
    )
    produto = models.ForeignKey(
        Produtos,
        on_delete=models.SET_NULL,
        related_name='produto_orcamentos',
        null=True,
        blank=True
    )
    patrimonio = models.ForeignKey(
        Patrimonio,
        on_delete=models.SET_NULL,
        related_name='patrimonio_orcamentos',
        null=True,
        blank=True
    )
    valor = models.DecimalField(
        'Valor',
        max_digits=6,
        decimal_places=2,
        blank=True,
        null=True
    )

    class Meta:
        ordering = ('-pk',)
        verbose_name = "Orçamento Item"
        verbose_name_plural = "Orçamento Itens"

    def __str__(self):
        return f'{self.pk}'
