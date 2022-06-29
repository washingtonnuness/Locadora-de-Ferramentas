from django.shortcuts import redirect, render

from .forms import ClientesForm
from .models import Clientes


def index(request):
    template_name = 'cliente_details.html'
    objects = Clientes.objects.all()
    context = {
        'object_list': objects,
    }
    return render(request, template_name, context)


def client_list(request):
    template_name = 'cliente_list.html'
    objects = Clientes.objects.all()
    context = {
        'object_list': objects,
    }
    return render(request, template_name, context)


def client_create(request):
    template_name = 'cliente_form_add_v2.html'
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
            return redirect('clientes:client_list')
        else:
            context = {
                'form': form,
            }
            return render(request, template_name, context)
