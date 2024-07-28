from django.http import HttpResponse

def inicio(request):
    return HttpResponse("Vista inicio")

def Mangas(request):
    return HttpResponse("Vista Mangas")

def Vendedores(request):
    return HttpResponse("Vista Vendedores")

def Usuarios(request):
    return HttpResponse("Vista Usuarios")


