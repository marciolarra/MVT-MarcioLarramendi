from django.shortcuts import render
from .models import Familiar
# Create your views here.

def primeraview(request):
    familiar_1 = Familiar(cedula_identidad=19751458, nombre_completo='Juan Pedro Lopez', fecha_nacimiento='09/03/1967')
    familiar_2 = Familiar(cedula_identidad=53688274, nombre_completo='Martin Lopez', fecha_nacimiento='26/05/1995')
    familiar_3 = Familiar(cedula_identidad=45781236, nombre_completo='Martina Lopez', fecha_nacimiento='10/12/1993')
    lista_familiares = [familiar_1, familiar_2, familiar_3]
    return render(request, 'index.html', {'familiares':lista_familiares})