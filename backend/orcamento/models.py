from django.db import models

from backend.cliente.models import Cliente
from backend.core.models import TimeStampedModel
from backend.produto.models import Patrimonio, Produto


class Orcamento(TimeStampedModel):
    cliente = models.ForeignKey(
        Cliente,
        on_delete=models.SET_NULL,
        related_name='cliente_orcamentos',
        null=True,
        blank=True
    )
    checkbox = models.BooleanField("Excluir", max_length=10)

    class Meta:
        ordering = ('created',)
        verbose_name = "Orçamento"
        verbose_name_plural = "Orçamentos"

    def __str__(self):
        return f'{self.pk}'


class OrcamentoItens(models.Model):
    orcamento = models.ForeignKey(
        Orcamento,
        on_delete=models.CASCADE,
        related_name='orcamentos',
    )
    produto = models.ForeignKey(
        Produto,
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
