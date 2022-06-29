from django.db import models


class Produto(models.Model):
    codigo = models.IntegerField("Código")
    id_grupo = models.ForeignKey(
        'Categoria',
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    id_marca = models.ForeignKey(
        'Marca',
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    nome = models.CharField("Nome", max_length=100)

    valor_Compra = models.DecimalField(
        'Preço compra',
        max_digits=6,
        decimal_places=2,
        blank=True,
        null=True
    )

    valor_Locacao = models.DecimalField(
        'Preço Diária',
        max_digits=6,
        decimal_places=2,
        blank=True,
        null=True
    )

    estoque_minimo = models.PositiveIntegerField(
        "Estoque minimo",
        null=True,
        blank=True
    )

    qnt_estoque = models.PositiveIntegerField(
        "Qnt em Estoque",
        null=True,
        blank=True
    )

    estoque_total = models.PositiveIntegerField(
        "Estoque total",
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
        max_length=100
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    delete_at = models.DateTimeField(
        auto_now=False,
        null=True
    )

    class Meta:
        verbose_name = "Produto"
        verbose_name_plural = "Produtos"
        ordering = ('id_grupo', 'id_marca', 'nome')

    def __str__(self):
        return f'{self.nome}'


class Patrimonio(models.Model):

    produtoPatrimonio = models.ForeignKey(
        Produto,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='patrimonios',
    )

    patrimonio = models.CharField(
        max_length=100,
        null=True,
        blank=True,
        unique=True,
    )

    class Meta:
        ordering = ('patrimonio',)

    def __str__(self):
        return f'{self.patrimonio}'


class Marca(models.Model):
    marca = models.CharField(
        max_length=100,
        unique=True
    )

    modelo = models.CharField(
        max_length=200,
        unique=False
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
        max_length=100
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    delete_at = models.DateTimeField(
        auto_now=False,
        null=True
    )

    class Meta:
        ordering = ('marca', 'modelo')

    def __str__(self):
        return f'{self.pk} - {self.marca} - {self.modelo}'


class Categoria(models.Model):

    categoria = models.CharField(
        max_length=100,
        unique=True
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
        max_length=100
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    delete_at = models.DateTimeField(
        auto_now=False,
        null=True
    )

    class Meta:
        ordering = ('categoria',)

    def __str__(self):
        return f'{self.categoria}'
