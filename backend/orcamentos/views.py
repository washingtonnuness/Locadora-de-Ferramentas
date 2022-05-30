from itertools import product

from django.contrib import messages
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.http import HttpResponse
from django.shortcuts import render

from backend.clientes.models import Clientes
from backend.produtos.forms import *
from backend.produtos.models import Patrimonio, Produtos

from .forms import OrcamentosForm
from .models import Orcamentos

# Create your views here.


def listOrcamentos(request):
    template_name = 'listarOrcamen.html'
    objects = Orcamentos.objects.all()
    context = {
        'object_list': '',
        'title': 'Listar Orçamentos',
    }
    return render(request, template_name, context)


def createorcamentos(request):
    template_name = 'orcamento_table.html'
    name = request.GET.get("searchField")

    if name == None:
        name = ''
        cliente = Clientes.objects.filter(nome__icontains=name)
        cliente = Clientes.objects.get(pk=id)
    else:
        # add film
        cliente = Clientes.objects.filter(nome__icontains=name)
        context = {
            'object_list': cliente,
            'title': 'Cadastro Orçamentos',
        }
        return render(request, template_name, context)
    # add the film to the user's list
    # request.user.filclientems.add(cliente)

    # return template fragment with all the user's films
    context = {
        'object_list': cliente,
        'title': 'Cadastro Orçamentos',
    }
    return render(request, template_name, context)


def add_orcamento(request, client_pk):
    template_name = 'orcamento_table.html'
    cliente = Clientes.objects.get(pk=client_pk)
    context = {'object_list': cliente}
    return render(request, template_name, context)


def search(request):
    template = 'orcamento_results_search.html'
    search_text = request.GET.get('search')
    results = Produtos.objects.filter(nome__icontains=search_text)

    context = {"results": results}
    return render(request, template, context)


def clear(request):
    return HttpResponse("")


def add_produtc_row(request, product_pk):
    template = 'orcamento_form_add.html'
    produto = Produtos.objects.get(pk=product_pk)
    productForm = OrcamentosForm()
    print(produto.codigo)
    context = {
        'object_list_product': produto,
        'productForm': productForm,
    }
    return render(request, template, context)


def order_update(request, product_pk):
    template_name = 'orcamento_form_add.html'
    obj = Produtos.objects.get(pk=product_pk)
    form = OrcamentosForm()
    #form = ProdutctForm(request.POST or None, prefix='main')

    context = {'form': form}
    return render(request, template_name, context)
