from django.db import models


class Clientes(models.Model):
    CNPJ = 'CNPJ'
    CPF = 'CPF'

    TIPO_REGISTRO = [
        (CNPJ, CNPJ),
        (CPF, CPF),
    ]

    tipo = models.CharField(
        max_length=4,
        choices=TIPO_REGISTRO,
        default=CNPJ,
    )

    cnpj = models.IntegerField(
        "CNPJ",
        null=True,
        blank=True
    )

    rg = models.IntegerField(
        "RG"
    )

    cpf = models.IntegerField(
        "CPF"
    )

    nome = models.CharField(
        "Nome Completo",
        max_length=250
    )

    razaoSocial = models.CharField(
        "Razão Social",
        max_length=250
    )

    nomeFantasia = models.CharField(
        "Nome Fantasia",
        max_length=250
    )

    endereco = models.CharField(
        "Endereço:",
        max_length=250
    )

    endereco2 = models.CharField(
        "Endereço Entrega:",
        max_length=250
    )

    cidade = models.CharField(
        "Cidade",
        max_length=100
    )

    estado = models.CharField(
        "Estado",
        max_length=100
    )

    cep = models.CharField(
        "Cep",
        max_length=100
    )

    delete_user = models.CharField(
        max_length=100,
        null=True,
        blank=True
    )

    checkbox = models.BooleanField(
        "Desativar",
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

    def is_upperclass(self):
        return self.tipo in {self.CNPJ, self.CPF}

    class Meta:
        ordering = ('tipo', 'nome', 'nomeFantasia')
        verbose_name = "Cliente"
        verbose_name_plural = "Clientes"

    def __str__(self):
        return f'{self.nome}'
