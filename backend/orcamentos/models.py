from django.db import models
from django.urls import reverse_lazy
from backend.clientes.models import Clientes
from backend.produtos.models import Produtos, Patrimonio


class Orcamentos(models.Model):
    cliente = models.ManyToManyField(
        Clientes,
        blank=True
    )

    produtos = models.ManyToManyField(
        Produtos,
        blank=True
    )
    patrimonio = models.ManyToManyField(
        Patrimonio,
        blank=True
    )
    valor = models.DecimalField('Valor', max_digits=6, decimal_places=2, blank=True, null=True)

    created_user = models.CharField(max_length=100, null=True, blank=True)
    delete_user = models.CharField(max_length=100, null=True, blank=True)

    checkbox = models.BooleanField("Excluir", max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    delete_at = models.DateTimeField(auto_now=False, null=True)

    class Meta:
        verbose_name = "Orçamento"
        verbose_name_plural = verbose_name+"s"
        ordering = ['created_at']

    def __str__(self):
        return '{} - {} - {}'.format(self.pk, self.produtos.nome, self.patrimonio)
