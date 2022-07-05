from random import choices

from django.core.management.base import BaseCommand
from faker import Faker

from backend.cliente.models import Cliente
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

        cliente.endereco2 = address()['street']

        cliente.city = _address['city']
        cliente.uf = _address['uf']
        cliente.cep = _address['cep']

        cliente.save()


class Command(BaseCommand):
    help = 'Corrige dados.'

    def handle(self, *args, **options):
        corrige_clientes()
