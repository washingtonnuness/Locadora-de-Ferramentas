from django.shortcuts import redirect, render

from .forms import ClienteForm
from .models import Cliente


def cliente_list(request):
    template_name = 'cliente_list.html'
    objects = Cliente.objects.all()
    context = {
        'object_list': objects,
    }
    return render(request, template_name, context)
