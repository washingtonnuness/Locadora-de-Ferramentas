from django.shortcuts import render

# Create your views here.


def index(request):
    template_name = 'index.html'
    # objects = EstoqueEntrada.objects.all()
    context = {
        # 'object_list': objects,
        'title': 'Principal',
        'url_add': 'core:'
    }
    return render(request, template_name, context)
