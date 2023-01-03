from django.shortcuts import render
from django.http import HttpResponse

from familia.models import Family


# Create your views here.
def create_family(request):
    Family.objects.create(name='Gabriel Peñaloza', age=64, married=True)
    return HttpResponse('Nuevo intgrate de la family2.0')

def list_family(request):
    all_family = Family.objects.all()
    print(all_family)
    context = {
        'family':all_family,
    }
    return render(request, 'list_family.html', context=context)