from django.http import HttpResponse # type: ignore
from datetime import datetime
from django.template import Template, Context # type: ignore


def saludo(request):
    return HttpResponse("Hola mundo!, soy Lautaro creando mi primer proyecto!")

def dia_de_hoy(request):
    dia = datetime.now()
    return HttpResponse(f"Hoy es día:<br>{dia}")

def muestra_nombre(request, nombre):
    return HttpResponse(f"Buenos días {nombre}, bienvenido a Coder")


def probando_template(request):

    # Abrimos el archivo html
    mi_html = open('./practica1/plantilla/index.html')

    # Creamos el template haciendo uso de la clase Template
    plantilla = Template(mi_html.read())

    # Cerramos el archivo previamente abierto, ya que lo tenemos cargado en la variable plantilla
    mi_html.close()

    # Creamos un contexto, más adelante vamos a aprender a usarlo, ahora lo necesitamos aunque sea vacío para que funcione
    mi_contexto = Context()

    # Terminamos de construír el template renderizándolo con su contexto
    documento = plantilla.render(mi_contexto)

    return HttpResponse(documento)