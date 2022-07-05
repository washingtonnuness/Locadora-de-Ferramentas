from random import choices

from django.core.management.base import BaseCommand
from faker import Faker

from backend.crm.models import Cliente, Fornecedor
from backend.orcamento.models import Orcamento, OrcamentoItens
from backend.produto.models import Categoria, Marca, Patrimonio, Produto
from backend.utils import utils as u

fake = Faker()
fake_ptbr = Faker('pt-br')


def address():
    address = fake_ptbr.address()
    address_list = address.split('\n')
    street = address_list[0]
    city = ' '.join(address_list[2].split()[1:-2])
    uf = address_list[2].split()[-1]
    cep = address_list[2].split()[0]
    return {
        'street': street,
        'city': city,
        'uf': uf,
        'cep': cep,
    }


def corrige_clientes():
    clientes = Cliente.objects.all()
    for cliente in clientes:
        cliente.tipo = choices(('CPF', 'CNPJ'))[0]
        if cliente.tipo == 'CPF':
            cliente.cpf = u.gen_cpf()
            cliente.cnpj = None
        else:
            cliente.cpf = None
            cliente.cnpj = u.gen_cnpj()

        cliente.rg = u.gen_rg()
        cliente.nome = fake.name()
        cliente.razao_social = fake.name()
        cliente.nome_fantasia = fake.name()

        _address = address()
        cliente.address = _address['street']
        cliente.district = fake_ptbr.bairro()

        cliente.endereco_entrega = address()['street']

        cliente.city = _address['city']
        cliente.uf = _address['uf']
        cliente.cep = _address['cep']

        cliente.save()


def corrige_fornecedores():
    fornecedores = Fornecedor.objects.all()
    for fornecedor in fornecedores:
        fornecedor.tipo = choices(('CPF', 'CNPJ'))[0]
        if fornecedor.tipo == 'CPF':
            fornecedor.cpf = u.gen_cpf()
            fornecedor.cnpj = None
        else:
            fornecedor.cpf = None
            fornecedor.cnpj = u.gen_cnpj()

        fornecedor.rg = u.gen_rg()
        fornecedor.nome = fake.name()
        fornecedor.razao_social = fake.name()
        fornecedor.nome_fantasia = fake.name()

        _address = address()
        fornecedor.address = _address['street']
        fornecedor.district = fake_ptbr.bairro()

        fornecedor.endereco_entrega = address()['street']

        fornecedor.city = _address['city']
        fornecedor.uf = _address['uf']
        fornecedor.cep = _address['cep']

        fornecedor.save()


def corrige_categorias():
    categorias = Categoria.objects.all()
    for categoria in categorias:
        _categoria = categoria.titulo.split()[:3]
        categoria.titulo = ' '.join(_categoria)
        categoria.save()


def corrige_marcas():
    marcas = Marca.objects.all()
    for marca in marcas:
        titulo = marca.titulo.split()[:3]
        marca.titulo = ' '.join(titulo)
        modelo = marca.modelo.split()[:3]
        marca.modelo = ' '.join(modelo)
        marca.save()


def corrige_patrimonios():
    patrimonios = Patrimonio.objects.all()
    for patrimonio in patrimonios:
        titulo = patrimonio.titulo.split()[:3]
        patrimonio.titulo = ' '.join(titulo)
        produtos = Produto.objects.all()
        produto = choices(produtos)[0]
        patrimonio.produto = produto
        patrimonio.save()


def corrige_produtos():
    produtos = Produto.objects.all()
    for produto in produtos:
        titulo = produto.titulo.split()[:3]
        produto.titulo = ' '.join(titulo)
        produto.save()


def corrige_orcamentos():
    orcamentos = Orcamento.objects.all()
    for orcamento in orcamentos:
        clientes = Cliente.objects.all()
        cliente = choices(clientes)[0]
        orcamento.cliente = cliente
        orcamento.save()


def corrige_orcamento_itens():
    orcamento_itens = OrcamentoItens.objects.all()
    for orcamento in orcamento_itens:
        produtos = Produto.objects.all()
        produto = choices(produtos)[0]
        orcamento.produto = produto

        patrimonios = Patrimonio.objects.all()
        patrimonio = choices(patrimonios)[0]
        orcamento.patrimonio = patrimonio

        orcamento.save()


class Command(BaseCommand):
    help = 'Corrige dados.'

    def handle(self, *args, **options):
        corrige_clientes()
        corrige_fornecedores()
        corrige_categorias()
        corrige_marcas()
        corrige_patrimonios()
        corrige_produtos()
        corrige_orcamentos()
        corrige_orcamento_itens()
