from django.shortcuts import render
from django.http import HttpResponse
from AppTerminal.models import Mangas
from AppTerminal.forms import MangasFormulario

def inicio(request):
    return render(request, "AppTerminal/index.html")

def Mangas(request):
    return render(request, "AppTerminal/Mangas.html")

def Vendedores(request):
    return render(request, "AppTerminal/Vendedores.html")

def Usuarios(request):
    return render(request, "AppTerminal/Usuarios.html")


def mangas_formulario(request):

    if request.method == 'POST':

        mangas = Mangas(nombre=request.POST['mangas'],tomos=request.POST['tomos'])
        mangas.save()

        return render(request, "AppTerminal/index.html")

    return render(request,"AppTerminal/mangas_formulario.html")



def form_con_api(request):
    if request.method == "POST":
        mi_formulario = MangasFormulario(request.POST) # Aqui me llega la informacion del html
        # print(miFormulario)
        if mi_formulario.is_valid():
            informacion = mi_formulario.cleaned_data
            
            mangas = Mangas(nombre=informacion["mangas"], tomos=informacion["tomos"])
            mangas.save()

            return render(request, "AppTerminal/index.html")
    else:
        mi_formulario = MangasFormulario()

    return render(request, "AppTerminal/form_con_api.html", {"mi_formulario": mi_formulario})


