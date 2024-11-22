from django.http import HttpResponse
from datetime import datetime


def saludo(request):
    return HttpResponse("Hola mundo!, soy Lautaro creando mi primer proyecto!")

def dia_de_hoy(request):
    dia = datetime.now()
    return HttpResponse(f"Hoy es día:<br>{dia}")

def muestra_nombre(request, nombre):
    return HttpResponse(f"Buenos días {nombre}, bienvenido a Coder")
