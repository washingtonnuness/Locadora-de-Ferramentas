from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from .forms import FornecedoresForm
from .models import Fornecedores


@login_required
def fornecedores_list(request):
    template_name = 'fornecedores_list.html'
    objects = Fornecedores.objects.all()
    context = {
        'object_list': objects,
    }
    return render(request, template_name, context)


@login_required
def fornecedores_create(request):
    template_name = 'fornecedores_form_add_v2.html'
    fornecedorForm = FornecedoresForm
    context = {
        'form': fornecedorForm,
    }
    return render(request, template_name, context)
