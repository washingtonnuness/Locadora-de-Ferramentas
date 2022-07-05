from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# Create your views here.


@login_required
def index(request):
    template_name = 'site2/index.html'
    context = {
        'url_add': 'core:',
        'user': 'Washington Nunes',
        'profile': 'Administrador',
        'user_email': 'washington.nunes@servilub.com.br'
    }
    return render(request, template_name, context)
