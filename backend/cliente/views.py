from django.shortcuts import redirect, render

from .forms import ClientesForm
from .models import Clientes


def cliente_list(request):
    template_name = 'cliente_list.html'
    objects = Clientes.objects.all()
    context = {
        'object_list': objects,
    }
    return render(request, template_name, context)
