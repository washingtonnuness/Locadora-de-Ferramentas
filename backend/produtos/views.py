from django.forms import inlineformset_factory
from django.shortcuts import redirect, render
#Importando do Forms os formulários criados.
from .forms import ProdutoForm, ProdutoPatrimonioForm, ProdutoItemsFormset
#Realizando o importo no models da classes para Produtos e patrimonio
from .models import Produtos, Patrimonio

# Create your views here.
def product_list(request):
    template_name = 'produto/produto_list.html'
    objects = Produtos.objects.all()
    context = {
        'object_list': objects,
        'title': 'Listar Produtos',
    }

    return render(request, template_name, context)

def product_create(request):
    template_name = 'produto/order_form.html'
    order_instance = Produtos()

    form = ProdutoForm(request.POST or None, instance=order_instance, prefix='main')
    formset = ProdutoItemsFormset(request.POST or None, instance=order_instance, prefix='items')

    if request.method == 'POST':
        print(formset)
        if form.is_valid() and formset.is_valid():
            form.save()
            formset.save()
            return redirect('produto:product_list')

    context = {'form': form, 'formset': formset}
    return render(request, template_name, context)


def add_row_product_items_hx(request):
    template_name = 'produto/hx/row_produtc_items_hx.html'
    form = ProdutoPatrimonioForm()
    context = {'order_item_form': form}
    return render(request, template_name, context)


def order_item_delete(request, pk):
    order_item = Produtos.objects.get(pk=pk)
    order_item.delete()
    return HttpResponse('')
