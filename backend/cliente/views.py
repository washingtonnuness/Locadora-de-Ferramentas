from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from .forms import ClienteForm
from .models import Cliente

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
        'form' : clienteForm,
    }
    return render(request, template_name, context)

