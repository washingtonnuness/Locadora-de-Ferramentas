from django.http import HttpResponse
from django.shortcuts import redirect, render

from .forms import PatrimonioForm, ProdutoForm, ProdutoItemsFormset
from .models import Produto


def produto_list(request):
    template_name = 'produto/produto_list.html'
    objects = Produto.objects.all()
    context = {
        'object_list': objects,
    }

    return render(request, template_name, context)


def produto_create(request):
    template_name = 'produto/produto_form.html'
    produto_instance = Produto()

    form = ProdutoForm(request.POST or None, instance=produto_instance, prefix='main')  # noqa E501
    formset = ProdutoItemsFormset(request.POST or None, instance=produto_instance, prefix='items')  # noqa E501

    if request.method == 'POST':
        if form.is_valid() and formset.is_valid():
            form.save()
            formset.save()
            return redirect('produto:produto_list')

    context = {'form': form, 'formset': formset}
    return render(request, template_name, context)


def add_row_produto_items_hx(request):
    template_name = 'produto/hx/row_produto_items_hx.html'
    form = PatrimonioForm()
    context = {'produto_item_form': form}
    return render(request, template_name, context)


def order_item_delete(request, pk):
    order_item = Produto.objects.get(pk=pk)
    order_item.delete()
    return HttpResponse('')
