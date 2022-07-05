from django.db import models

from backend.core.models import Active, CreatedBy, DeletedBy, TimeStampedModel


class Produto(TimeStampedModel, CreatedBy, DeletedBy, Active):
    codigo = models.IntegerField('Código')
    titulo = models.CharField('titulo', max_length=100)
    categoria = models.ForeignKey(
        'Categoria',
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    marca = models.ForeignKey(
        'Marca',
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    preco_compra = models.DecimalField(
        'Preço compra',
        max_digits=6,
        decimal_places=2,
        blank=True,
        null=True
    )
    preco_diaria = models.DecimalField(
        'Preço Diária',
        max_digits=6,
        decimal_places=2,
        blank=True,
        null=True
    )
    estoque_minimo = models.PositiveIntegerField('Estoque Mínimo', null=True, blank=True)  # noqa E501
    estoque_atual = models.PositiveIntegerField('Estoque Atual', null=True, blank=True)  # noqa E501

    class Meta:
        ordering = ('titulo',)
        verbose_name = 'Produto'
        verbose_name_plural = 'Produtos'

    def __str__(self):
        return f'{self.titulo}'


class Patrimonio(TimeStampedModel, CreatedBy, DeletedBy, Active):
    titulo = models.CharField('titulo', max_length=100, unique=True)
    produto = models.ForeignKey(
        Produto,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='patrimonios',
    )

    class Meta:
        ordering = ('titulo',)
        verbose_name = 'Patrimônio'
        verbose_name_plural = 'Patrimônios'

    def __str__(self):
        return f'{self.titulo}'


class Marca(TimeStampedModel, CreatedBy, DeletedBy, Active):
    titulo = models.CharField(max_length=100, unique=True)
    modelo = models.CharField(max_length=200)

    class Meta:
        ordering = ('titulo',)

    def __str__(self):
        return f'{self.titulo}'


class Categoria(TimeStampedModel, CreatedBy, DeletedBy, Active):
    titulo = models.CharField(max_length=100, unique=True)

    class Meta:
        ordering = ('titulo',)

    def __str__(self):
        return f'{self.titulo}'
