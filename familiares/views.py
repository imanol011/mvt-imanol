from django.shortcuts import render
from django.http import HttpResponse

def lista_familiares(request):
    contex = {
        'nombre_1': 'Gabriel',
        'edad_1':64,
        'casado_1': True,
        'nombre_2': 'Ema',
        'edad_2':66,
        'casado_2': True,
        'nombre_3': 'Imanol',
        'edad_3':25,
        'casado_3': False
    }
    return render(request, 'familiares.html', context=contex)