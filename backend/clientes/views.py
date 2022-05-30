from django.shortcuts import render
from django.shortcuts import redirect, render
from .models import Clientes
from .forms import ClientesForm
# Create your views here.


def index(request):
    template_name = 'formClientes.html'
    objects = Clientes.objects.all()
    context = {
        'object_list': objects,
        'title': 'Cadastro de Clientes',
    }
    return render(request, template_name, context)


def listarClientes(request):
    template_name = 'listarCliente.html'
    objects = Clientes.objects.all()
    context = {
        'object_list': objects,
        'title': 'Clientes',
    }
    return render(request, template_name, context)


def inserir(request):
    template_name = 'formClientes.html'
    if request.method == "GET":
        form = ClientesForm()
        context = {
            'form': form,
        }
        return render(request, template_name, context)

    elif request.method == "POST":
        form = ClientesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('clientes:listarClientes')
        else:
            context = {
                'form': form,
            }
            return render(request, template_name, context)
