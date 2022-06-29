from django.contrib import messages
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render

from backend.cliente.models import Clientes
from backend.produto.forms import *
from backend.produto.models import Patrimonio, Produtos

from .forms import OrcamentosForm, OrcamentosFormSet
from .models import Orcamentos, OrcamentosItens

# Create your views here.


def orcamento_list(request):
    template_name = 'orcamento_list.html'
    objects = Orcamentos.objects.all()
    context = {
        'object_list': objects,
    }
    return render(request, template_name, context)


def orcamento_create(request, client_pk):
    template_name = 'orcamento_form_add.html'
    name = request.GET.get("searchField")

    if name == None:
        name = ''
        cliente = Clientes.objects.filter(nome__icontains=name)
        cliente = Clientes.objects.get(pk=client_pk)
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
    template_name = 'orcamento_form_add.html'
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


def add_row_hx(request, pk):
    template = 'orcamento_list.html'
    produto = Produtos.objects.get(pk=pk)
    form = OrcamentosFormSet()

    context = {
        'form': form,
        'object_list_product': produto,
    }
    return render(request, template, context)


def order_update(request, pk):
    template_name = 'orcamento_form_add.html'
    obj = Produtos.objects.get(pk=pk)
    form = OrcamentosForm(isinstance=obj)
    context = {'form': form}
    return render(request, template_name, context)


def post_update(request, id):
    product = get_object_or_404(Produtos, pk=id)
    form = Produtos(instance=product)
    if(request.method == 'POST'):
        form = Produtos(request.POST, instance=product)

        if(form.is_valid()):
            post = form.save(commit=False)
            post.title = form.cleaned_data['title']
            post.description = form.cleaned_data['slug']
            post.body = form.cleaned_data['body']
            post.author = form.cleaned_data['author']
            post.status = form.cleaned_data['status']
            post.save()
            return redirect('blog:post_list')
        else:
            return render(request, 'blog/edit_post.html', {'form': form, 'post': post})
    elif(request.method == 'GET'):
        return render(request, 'blog/edit_post.html', {'form': form, 'post': post})
