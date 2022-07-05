from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# Create your views here.


@login_required
def index(request):
    template_name = 'site2/index.html'
    context = {
    }
    return render(request, template_name, context)
