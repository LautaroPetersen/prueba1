from django.http import HttpResponse

def saludo(request):
    return HttpResponse("Hola mundo!, soy Lautaro creando mi primer proyecto!")