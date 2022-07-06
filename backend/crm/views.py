from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin as LRM
from django.shortcuts import render
from django.views.generic import CreateView, DetailView, ListView, UpdateView

from .forms import ClienteForm, FornecedorForm
from .models import Cliente, Fornecedor


@login_required
def cliente_list(request):
    template_name = 'cliente_list.html'
    objects = Cliente.objects.all()
    context = {
        'object_list': objects,
    }
    return render(request, template_name, context)


@login_required
def cliente_create(request):
    template_name = 'cliente_form_add_v2.html'
    clienteForm = ClienteForm
    context = {
        'form': clienteForm,
    }
    return render(request, template_name, context)


class FornecedorListView(LRM, ListView):
    model = Fornecedor


class FornecedorDetailView(LRM, DetailView):
    model = Fornecedor


class FornecedorCreateView(LRM, CreateView):
    model = Fornecedor
    form_class = FornecedorForm
