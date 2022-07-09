from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin as LRM
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, ListView, UpdateView

from backend.crm.models import Cliente
from backend.produto.forms import CategoriatForm, MarcaForm, ProdutoForm
from backend.produto.models import Produto

from .forms import OrcamentoForm, OrcamentoFormSet
from .models import Orcamento, OrcamentoItens


class OrcamentoListView(LRM, ListView):
    model = Orcamento


@login_required
def orcamento_create(request, client_pk):
    cliente = Cliente.objects.get(pk=client_pk)
    orcamento = Orcamento.objects.create(cliente=cliente)
    return redirect(reverse_lazy('orcamento:orcamento_update', kwargs={'pk': orcamento.pk}))  # noqa E501


@login_required
def orcamento_update(request, pk):
    template_name = 'orcamento/orcamento_form.html'
    orcamento = Orcamento.objects.get(pk=pk)
    context = {'object': orcamento}
    return render(request, template_name, context)


@login_required
def search(request):
    template = 'hx/orcamento_results_search.html'
    search_text = request.GET.get('search')
    results = Produto.objects.filter(titulo__icontains=search_text)

    context = {"results": results}
    return render(request, template, context)


@login_required
def invoice(request):
    template = 'orcamento/orcamento_invoice.html'
    results = ''

    context = {"results": results}
    return render(request, template, context)


@login_required
def clear(request):
    return HttpResponse("")


@login_required
def add_row_hx(request, pk):
    template = 'hx/orcamento_table.html'
    produto = Produto.objects.get(pk=pk)
    form = OrcamentoFormSet()

    context = {
        'form': form,
        'object_list_product': produto,
    }
    return render(request, template, context)


@login_required
def order_update(request, pk):
    template_name = 'orcamento_form_add.html'
    obj = Produto.objects.get(pk=pk)
    form = OrcamentoForm(isinstance=obj)
    context = {'form': form}
    return render(request, template_name, context)


@login_required
def post_update(request, id):
    product = get_object_or_404(Produto, pk=id)
    form = Produto(instance=product)
    if(request.method == 'POST'):
        form = Produto(request.POST, instance=product)

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
