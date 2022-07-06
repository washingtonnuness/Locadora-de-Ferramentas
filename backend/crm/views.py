from django.contrib.auth.mixins import LoginRequiredMixin as LRM
from django.views.generic import CreateView, DetailView, ListView, UpdateView

from .forms import ClienteForm, FornecedorForm
from .models import Cliente, Fornecedor


class ClienteListView(LRM, ListView):
    model = Cliente


class ClienteDetailView(LRM, DetailView):
    model = Cliente


class ClienteCreateView(LRM, CreateView):
    model = Cliente
    form_class = ClienteForm


class FornecedorListView(LRM, ListView):
    model = Fornecedor


class FornecedorDetailView(LRM, DetailView):
    model = Fornecedor


class FornecedorCreateView(LRM, CreateView):
    model = Fornecedor
    form_class = FornecedorForm
