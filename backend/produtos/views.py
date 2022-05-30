from django.shortcuts import redirect, render
from .models import Produtos, Patrimonio
from django.forms import inlineformset_factory

from .forms import ProdutctForm, PatrimonioForm, ProdutoFormset

# Create your views here.


def index(request):
    template_name = 'formProdutos.html'
    # forms = ProdutctForm(request.POST or None)
    # objects = EstoqueEntrada.objects.all()
    context = {
        # 'object_list': objects,
        'title': 'Cadastro de Produtos',
    }
    return render(request, template_name, context)


def listProdutos(request):
    template_name = 'listarProdutos.html'
    objects = Produtos.objects.all()
    context = {
        'object_list': objects,
        'title': 'Listar Produtos',
        'url_add': 'produtos:'
    }
    return render(request, template_name, context)


def inserir(request):
    template_name = 'form.html'
    if request.method == "GET":
        form = ProdutctForm()
        form_telefone_factory = inlineformset_factory(
            Produtos, Patrimonio, form=ProdutctForm, extra=1)
        form_telefone = form_telefone_factory()
        context = {
            'form': form,
            'formset': form_telefone,
        }
        return render(request, template_name, context)

    elif request.method == "POST":
        form = ProdutctForm(request.POST)
        form_telefone_factory = inlineformset_factory(
            Produtos, Patrimonio, form=PatrimonioForm)
        form_telefone = form_telefone_factory(request.POST)
        if form.is_valid() and form_telefone.is_valid():
            ocorrencia = form.save()
            form_telefone.instance = ocorrencia
            form_telefone.save()
            return redirect('core:index')
        else:
            context = {
                'form': form,
                'formset': form_telefone,
            }
            return render(request, template_name, context)


def order_item_delete(request, pk):
    order_item = Produtos.objects.get(pk=pk)
    order_item.delete()
    return HttpResponse('asdfasdfasdf')
